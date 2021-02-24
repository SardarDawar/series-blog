from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.http import JsonResponse, request
from operator import attrgetter
from .models import *
from .filters import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





def homeView(request):

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        if query:
            query = str(query)

    

    slides = Slider.get_all_slides()
    content = searchContent(query)
    content = sorted(content, key = attrgetter('orderBy'), reverse=True)
                ########################### PAGINATION ##################
    paginator = Paginator(content ,100) # Shows only 10 records per page

    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        content = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 7777), deliver last page of results.
        content = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'contents':content, 'query': query, 'slides': slides})



def autocomp(request):

    #qs = []
    names = list()
    if 'term' in request.GET:
        qs = Movie.objects.filter(name__icontains=request.GET.get('term'))
        for content in qs:
            names.append(content.name)
        qs = Series.objects.filter(name__icontains=request.GET.get('term'))
        for content in qs:
            names.append(content.name)
        qs = Playlist.objects.filter(name__icontains=request.GET.get('term'))
        for content in qs:
            names.append(content.name)
        qs = NewArrival.objects.filter(name__icontains=request.GET.get('term'))
        for content in qs:
            names.append(content.name)
        qs = ComingSoon.objects.filter(name__icontains=request.GET.get('term'))
        for content in qs:
            names.append(content.name)
    
    
    return JsonResponse(names, safe=False)

    

    

    return render(request, 'home.html', {'contents':content, 'query': query, 'slides': slides})








def movie(request):
    content = Movie.get_all_movies()
    movieFilter = MovieFilter(request.GET, queryset = content)
    content = movieFilter.qs
    categories = MovieCategory.get_all_categories()
    genres = Genre.get_all_genres()
                ########################### PAGINATION ##################
    paginator = Paginator(content ,50) # Shows only 10 records per page

    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        content = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 7777), deliver last page of results.
        content = paginator.page(paginator.num_pages)
    return render(request, 'movie.html', {'contents':content, 'categories': categories, 'genres': genres})


# def filter(request):
#     content = Movie.get_all_movies()
#     kk = request.GET
#     print('request get=',kk)
#     movieFilter = MovieFilter(kk, queryset = content)
#     content = movieFilter.qs
#     data = content.values()
#     return JsonResponse(list(data), safe=False)




def series(request):
    content = Series.get_all_series()
    seriesFilter = SeriesFilter(request.GET, queryset = content)
    content = seriesFilter.qs
    categories = SeriesCategory.get_all_categories()
    genres = Genre.get_all_genres()
    return render(request, 'series.html', {'contents':content, 'categories': categories, 'genres': genres})
    
def playlist(request):
    content = Playlist.get_all_playlist()
    playlistFilter = PlaylistFilter(request.GET, queryset = content)
    content = playlistFilter.qs
    categories = PlaylistCategory.get_all_categories()
    genres = Genre.get_all_genres()
    return render(request, 'playlist.html', {'contents':content, 'categories': categories, 'genres': genres})

def comingSoon(request):
    content = ComingSoon.get_all_comingSoon()
    comingSoonFilter = ComingSoonFilter(request.GET, queryset = content)
    content = comingSoonFilter.qs
    movieCat = MovieCategory.get_all_categories()
    serCat = SeriesCategory.get_all_categories()
    playCat = PlaylistCategory.get_all_categories()
    genres = Genre.get_all_genres()
    return render(request, 'coming_soon.html', {'contents':content, 'movieCat': movieCat,'serCat': serCat,'playCat': playCat, 'genres': genres})

def newArrival(request):
    content = NewArrival.get_all_arrivals()
    newArrivalFilter = NewArrivalFilter(request.GET, queryset = content)
    content = newArrivalFilter.qs
    movieCat = MovieCategory.get_all_categories()
    serCat = SeriesCategory.get_all_categories()
    playCat = PlaylistCategory.get_all_categories()
    genres = Genre.get_all_genres()
    return render(request, 'newarrival.html', {'contents':content, 'movieCat': movieCat,'serCat': serCat,'playCat': playCat, 'genres': genres})



def movieProfile(request, slug):
    try:
        episodes = Season.get_all_seasons(slug)
        if not episodes:
            episodes = Episode.get_all_episodes(slug)

        elif len(episodes) == 1:
             episodes = Episode.get_all_episodes(slug)
             return render(request, 'episodes.html', {'episodes': episodes})

    except:
        episodes = Playlist_items.get_playlist_items(slug)
    
    return render(request, 'movieprofile.html', {'episodes': episodes})



def episodeView(request, slug):
    try:
        episodes = Episode.get_episodes_by_season(slug)
    except:
        episodes = Playlist_items.get_playlist_items(slug)

    return render(request, 'episodes.html', {'episodes': episodes})





def Video(request, slug):
    try:
        episode = Episode.objects.get(slug=slug)
        comments = Comment.get_all_epi_comments(slug)
        return render(request, 'video.html', {'episode': episode, 'comments': comments})
    except:
        try:
            episode = Playlist_items.objects.get(slug=slug)
            comments = Comment.get_all_pl_comments(slug)
            return render(request, 'video.html', {'episode': episode, 'comments': comments})
        except:
            try:
                episode = Movie.objects.get(slug=slug)
                comments = Comment.get_all_mv_comments(slug)
                return render(request, 'movie_video.html', {'episode': episode, 'comments': comments})
            except:
                episode = NewArrival.objects.get(slug=slug)
                comments = Comment.get_all_na_comments(slug)
                return render(request, 'movie_video.html', {'episode': episode, 'comments': comments})
    


def CommentView(request, slug):
    if request.method == 'POST':
        
        
        email = request.POST.get('email')
        name = request.POST.get('name')
        c_body = request.POST.get('c_body')
        try:
            episode = Episode.objects.get(slug=slug)
            Comment.objects.create(episode= episode, commentator= email, body = c_body, com_name = name)
        except:
            try:
                episode = Playlist_items.objects.get(slug=slug)
                Comment.objects.create(playlist_item= episode, commentator= email, body = c_body, com_name = name)
            except:
                try:
                    episode = Movie.objects.get(slug=slug)
                    Comment.objects.create(movie= episode, commentator= email, body = c_body, com_name = name)
                except:
                    episode = NewArrival.objects.get(slug=slug)
                    Comment.objects.create(newarrival= episode, commentator= email, body = c_body, com_name = name)
        
        return JsonResponse({'status': 'Saved!'})
    else:
        return JsonResponse({'status': 'Error'})

def likeEp(request):
    if (request.method == 'POST'):
        slug = request.POST['slug']
        print('slug = ',slug)
        try:
            episode = Episode.objects.get(slug=slug)
            like = request.session.get('ep_like')
            chk = 1
        except:
            try:
                episode = Playlist_items.objects.get(slug=slug)
                like = request.session.get('pl_like')
                chk = 2
            except:
                try:
                    episode = Movie.objects.get(slug=slug)
                    like = request.session.get('mv_like')
                    chk = 3
                except:
                    episode = NewArrival.objects.get(slug=slug)
                    like = request.session.get('na_like')
                    chk = 4
        ep_id = str(episode.id)
        if like:
            quant = like.get(ep_id)
            print('quant=',quant)
            if quant:
                print('quant=',quant)
                if quant >= 1:
                    episode.likes-=1
                    episode.save()
                    like[ep_id] = 0
                    quant = like.get(ep_id)
                    print('quant2=',quant)
                else:
                    episode.likes+=1
                    episode.save()
                    like[ep_id] = 1
                    print('likee:',like)
            else:
                print('Ye ho rha he..')
                like[ep_id] = 1
                episode.likes+=1
                episode.save()
        else:
            like = {}
            episode.likes+=1
            episode.save()
            like[ep_id] = 1
        if chk == 1:
            request.session['ep_like'] = like
        elif chk == 2:
            request.session['pl_like'] = like
        elif chk == 3:
            request.session['mv_like'] = like
        elif chk == 4:
            request.session['na_like'] = like

        data = {
        'like': like,
        }

        return JsonResponse(data)


def clearSession(request):
    request.session.clear()
    return redirect('/')


def searchContent(query=None):
    queryset = []
    #val = [1,2,3,4,5]
    k = None
    queries = query.split(" ")
    for q in queries:
        contents = Movie.objects.filter(
                Q(name__icontains=q),
            ).distinct()
        for content in contents:
            #print(content.category.id)
            # for i in val:
            #     if content.category.id==i:
            queryset.append(content)

    for q in queries:
        contents = Series.objects.filter(
                Q(name__icontains=q),
            ).distinct()
        for content in contents:
            #print(content.category.id)
            # for i in val:
            #     if content.category.id==i:
            queryset.append(content)

    for q in queries:
        contents = Playlist.objects.filter(
                Q(name__icontains=q),
            ).distinct()
        for content in contents:
            #print(content.category.id)
            # for i in val:
            #     if content.category.id==i:
            queryset.append(content)

    for q in queries:
        contents = NewArrival.objects.filter(
                Q(name__icontains=q),
            ).distinct()
        for content in contents:
            #print(content.category.id)
            # for i in val:
            #     if content.category.id==i:
            queryset.append(content)


    return list(set(queryset))



def error_404_view(request, exception):
    return render(request, 'error_404.html')

def error_500_view(request):
    return render(request, 'error_500.html')



def movieFilter(request, slug):
    try:
        content = Movie.get_movies_by_category(slug)
    except:
        content = Movie.get_movies_by_genre(slug)
    categories = MovieCategory.get_all_categories()
    genres = Genre.get_all_genres()
                ########################### PAGINATION ##################
    paginator = Paginator(content ,50) # Shows only 10 records per page

    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        content = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 7777), deliver last page of results.
        content = paginator.page(paginator.num_pages)
    return render(request, 'movie.html', {'contents':content, 'categories': categories, 'genres': genres})

def seriesFilter(request, slug):
    try:
        content = Series.get_series_by_category(slug)
    except:
        content = Series.get_series_by_genre(slug)
    categories = SeriesCategory.get_all_categories()
    genres = Genre.get_all_genres()

    return render(request, 'series.html', {'contents':content, 'categories': categories, 'genres': genres})

def playlistFilter(request, slug):
    try:
        content = Playlist.get_playlist_by_category(slug)
    except:
        content = Playlist.get_playlist_by_genre(slug)
    categories = PlaylistCategory.get_all_categories()
    genres = Genre.get_all_genres()

    return render(request, 'playlist.html', {'contents':content, 'categories': categories, 'genres': genres})


def newArrFilter(request, slug):
    try:
        content = NewArrival.get_na_by_movie(slug)
    except:
        try:
            content = NewArrival.get_na_by_series(slug)
        except:
            try:
                content = NewArrival.get_na_by_playlist(slug)
            except:
                content = NewArrival.get_na_by_genre(slug)
    movieCat = MovieCategory.get_all_categories()
    serCat = SeriesCategory.get_all_categories()
    playCat = PlaylistCategory.get_all_categories()
    genres = Genre.get_all_genres()
    return render(request, 'newarrival.html', {'contents':content, 'movieCat': movieCat,'serCat': serCat,'playCat': playCat, 'genres': genres})


def comingSoonFilter(request, slug):
    try:
        content = ComingSoon.get_cs_by_movie(slug)
    except:
        try:
            content = ComingSoon.get_cs_by_series(slug)
        except:
            try:
                content = ComingSoon.get_cs_by_playlist(slug)
            except:
                content = ComingSoon.get_cs_by_genre(slug)
    movieCat = MovieCategory.get_all_categories()
    serCat = SeriesCategory.get_all_categories()
    playCat = PlaylistCategory.get_all_categories()
    genres = Genre.get_all_genres()
    return render(request, 'coming_soon.html', {'contents':content, 'movieCat': movieCat,'serCat': serCat,'playCat': playCat, 'genres': genres})

def detail(request, slug):
    episodes = None
    try:
        content = Movie.objects.get(slug=slug)
        comments = Comment.get_all_mv_comments(slug)
        return render(request, 'detail.html', {'content': content, "comments":comments})


    except:
        try:
            content = Series.objects.get(slug=slug)
            episodes = Season.get_all_seasons(slug)
        except:
            try:
                content = Playlist.objects.get(slug=slug)
                episodes = Playlist_items.get_playlist_items(slug)
            except:
                try:
                    content = NewArrival.objects.get(slug=slug)
                except:
                    content = ComingSoon.objects.get(slug=slug)
                    return render(request, 'coming_soon_detail.html', {'content': content})

    
    return render(request, 'detail.html', {'content': content, 'episodes': episodes,})

##############################################################################################
import requests
from bs4 import BeautifulSoup
def slug_converter(name):
    lowercase = name.lower()
    return (lowercase.replace(' ','-'))

    
def scrape_data(link):
        # URL to scrape
    url = link
    # request
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # category
    category = soup.find('i',class_="limpiar").text
    category_check = category.find('Hindi')
    # variables
    info = soup.find('div',class_="fix")
    image = info.find('img')['data-lazy-src']
    try:
        quality = info.find('span').text
    except:
        quality = "N/A"
    data = soup.find('div',class_="data")
    movie_name = data.find('h1').text
    print(movie_name)
    try:
        meta_name = data.find_all(itemprop="name")[1].text
    except:
        meta_name = movie_name
    release_date = data.find(itemprop="datePublished").text
    length = data.find(itemprop="duration").text
    try:
        rating = soup.find(itemprop="ratingValue").text
        ratingCount = soup.find(itemprop="ratingCount").text
    except:
        rating = "N/A"
    synopsis_sc = soup.find_all("p")[6:8]
    synopsis = ''.join(map(str, synopsis_sc))

    metas = soup.find_all('div', class_="metatags" )
    try:
        directors = metas[0].find_all("a")
        directors_list = []
        [directors_list.append(i.text+",") for i in directors ]
        director = ''.join(map(str, directors_list))
    except:
        directors = "N/A"
    try:
        stars = metas[1].find_all("a")
        stars_list = []
        [stars_list.append(i.text+",") for i in stars ]
        cast = ''.join(map(str, stars_list))
    except:
        cast = "N/A"
    #form fields
    try:
        fname = soup.find('input',{"name":"FName"}).get('value')
        fsize = soup.find('input',{"name":"FSize"}).get('value')
        fsid = soup.find('input',{"name":"FSID"}).get('value')
        print(fname, fsize, fsid)
    except:
        fname = 'upcoming'
        fsize = 'upcoming'
        fsid  = 'upcoming'
    slug=slug_converter(movie_name)
    
    check_variable = True
    for i in Movie.objects.all():
        if i.slug == slug:
            check_variable= False
    if check_variable == True:
        if category_check == -1:
            Movie.objects.create(category_id=1,genre_id=4,name=movie_name,slug=slug,meta_name=meta_name,description=synopsis,img_url=image,rating=rating, quality=quality,language="Hindi",cast=cast ,length=length, director=director,fname=fname,fsize=fsize,fsid=fsid,release_date=release_date,orderBy=1,likes=0)
        else:
            Movie.objects.create(category_id=2,genre_id=4,name=movie_name,slug=slug_converter(movie_name),meta_name=meta_name,description=synopsis,img_url=image,rating=rating, quality=quality,language="English",cast=cast ,length=length, director=director,fname=fname,fsize=fsize,fsid=fsid,release_date=release_date,orderBy=1,likes=0)


#    content = [movie_name,full_name,size,quality,genre,release_date,language,cast,text_info, text_synopsis_1, text_synopsis_2]

def data(request):

    for i in range(1,17):
        url = "https://www.foumovies.se/category/comedy/page/{}/".format(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        info = soup.find_all('div', class_="item")
        print(i)

        for i in info:
            image = i.find('img')['data-lazy-src']
            link = i.find('a')['href']
            scrape_data(link)
    return 0


def news(request):
    Movie.objects.create(category_id=1,genre_id=1,name='kuch bhu', slug='kuch-bhi',description="hgbnj",img_url="https://moviescounter.se/wp-content/uploads/2021/02/Untitled-1-Recovered-230x340.jpg",size="1gb", quality="jj",language="eng",cast="kud",poster_url="https://moviescounter.se/wp-content/uploads/2021/02/Untitled-1-Recovered-230x340.jpg",PG='45',release_date="25 5",orderBy=2,likes=0)
    return 0


