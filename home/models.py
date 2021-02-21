from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from django.urls import reverse



class MovieCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='prod_imgs/')


    def get_all_categories():
        return MovieCategory.objects.all()

    def __str__(self):
        return self.name



class SeriesCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='prod_imgs/')


    def get_all_categories():
        return SeriesCategory.objects.all()

    def __str__(self):
        return self.name


class PlaylistCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='prod_imgs/')


    def get_all_categories():
        return PlaylistCategory.objects.all()

    def __str__(self):
        return self.name




class Genre(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='prod_imgs/')


    def get_all_genres():
        return Genre.objects.all()

    def __str__(self):
        return self.name



class Movie(models.Model):
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    genre_values = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    img = models.ImageField(upload_to='prod_imgs/',blank=True)
    img_url = models.URLField(blank=True)
    
    size = models.CharField(max_length=20)
    quality = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    cast = models.TextField()
    rating = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    src = models.TextField(blank=True)
    orderBy = models.FloatField()
    likes = models.IntegerField(blank=True)

    class Meta:
        ordering = ['-orderBy']

    def get_all_movies():
        return Movie.objects.all()

    def get_movies_by_category(slug):
        cat_id = MovieCategory.objects.get(slug=slug)
        return Movie.objects.filter(category=cat_id)

    def get_movies_by_genre(slug):
        gen_id = Genre.objects.get(slug=slug)
        return Movie.objects.filter(genre=gen_id)

    def __str__(self):
        return self.name + ' | ' + self.category.name

    def get_absolute_url(self):
        return reverse('video', args=[self.slug])



class Series(models.Model):
    category = models.ForeignKey(SeriesCategory, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    release_date = models.CharField(max_length=100)
    img = models.ImageField(upload_to='prod_imgs/')
    orderBy = models.FloatField()
    rating = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    quality = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    cast = models.TextField()

    class Meta:
        ordering = ['-orderBy']

    def get_all_series():
        return Series.objects.all()

    def get_series_by_category(slug):
        cat_id = SeriesCategory.objects.get(slug=slug)
        return Series.objects.filter(category=cat_id)

    def get_series_by_genre(slug):
        gen_id = Genre.objects.get(slug=slug)
        return Series.objects.filter(genre=gen_id)

    def __str__(self):
        return self.name + ' | ' + self.category.name

    def get_absolute_url(self):
        return reverse('movieprofile', args=[self.slug])


    

class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='prod_imgs/')
    orderBy = models.FloatField()

    class Meta:
        ordering = ['-orderBy']

    def get_all_seasons(slug):
        series_id = Series.objects.get(slug=slug)
        return Season.objects.filter(series = series_id)


    def __str__(self):
        return self.name + ' | ' + self.series.name

    def get_absolute_url(self):
        return reverse('epi', args=[self.slug])




class Episode(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    img = models.ImageField(upload_to='prod_imgs/')
    src = models.TextField()
    orderBy = models.FloatField()
    likes = models.IntegerField()

    class Meta:
        ordering = ['-orderBy']


    def get_all_episodes(slug):
        series_id = Series.objects.get(slug=slug)
        return Episode.objects.filter(series = series_id)

    def get_episodes_by_season(slug):
        if slug:
            se_id = Season.objects.get(slug=slug)
            return Episode.objects.filter(season = se_id)
        else:
            return Episode.objects.all()

    def get_absolute_url(self):
        return reverse('video', args=[self.slug])


class Playlist(models.Model):
    category = models.ForeignKey(PlaylistCategory, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    release_date = models.CharField(max_length=100)
    img = models.ImageField(upload_to='prod_imgs/')
    orderBy = models.FloatField()
    rating = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    quality = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    cast = models.TextField()
    poster = models.ImageField(upload_to='prod_imgs/')

    class Meta:
        ordering = ['-orderBy']

    def get_all_playlist():
        return Playlist.objects.all()

    def get_playlist_by_category(slug):
        cat_id = PlaylistCategory.objects.get(slug=slug)
        return Playlist.objects.filter(category=cat_id)

    def get_playlist_by_genre(slug):
        gen_id = Genre.objects.get(slug=slug)
        return Playlist.objects.filter(genre=gen_id)

    def __str__(self):
        return self.name + ' | ' + self.category.name

    def get_absolute_url(self):
        return reverse('movieprofile', args=[self.slug])





class Playlist_items(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    img = models.ImageField(upload_to='prod_imgs/')
    src = models.TextField()
    orderBy = models.FloatField()
    likes = models.IntegerField()

    class Meta:
        ordering = ['-orderBy']



    def get_playlist_items(slug):
        se_id = Playlist.objects.get(slug=slug)
        return Playlist_items.objects.filter(playlist = se_id)

    def get_absolute_url(self):
        return reverse('epi', args=[self.slug])

class ComingSoon(models.Model):
    movie = models.ForeignKey(MovieCategory, on_delete=models.CASCADE, null=True, blank=True)
    series = models.ForeignKey(SeriesCategory, on_delete=models.CASCADE, null=True, blank=True)
    playlist =  models.ForeignKey(PlaylistCategory, on_delete=models.CASCADE, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    release_date = models.CharField(max_length=100)
    img = models.ImageField(upload_to='prod_imgs/')
    orderBy = models.FloatField()
    size = models.CharField(max_length=20)
    rating = models.CharField(max_length=100)
    quality = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    cast = models.TextField()
    poster = models.ImageField(upload_to='prod_imgs/')

    def get_cs_by_movie(slug):
        cat_id = MovieCategory.objects.get(slug=slug)
        return ComingSoon.objects.filter(movie=cat_id)

    def get_cs_by_series(slug):
        cat_id = SeriesCategory.objects.get(slug=slug)
        return ComingSoon.objects.filter(series=cat_id)

    def get_cs_by_playlist(slug):
        cat_id = PlaylistCategory.objects.get(slug=slug)
        return ComingSoon.objects.filter(playlist=cat_id)

    def get_cs_by_genre(slug):
        gen_id = Genre.objects.get(slug=slug)
        return ComingSoon.objects.filter(genre=gen_id)

    class Meta:
        ordering = ['-orderBy']

    def get_all_comingSoon():
        return ComingSoon.objects.all()

    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movieprofile', args=[self.slug])


class NewArrival(models.Model):
    movie = models.ForeignKey(MovieCategory, on_delete=models.CASCADE, null=True, blank=True)
    series = models.ForeignKey(SeriesCategory, on_delete=models.CASCADE, null=True, blank=True)
    playlist =  models.ForeignKey(PlaylistCategory, on_delete=models.CASCADE, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    release_date = models.CharField(max_length=100)
    img = models.ImageField(upload_to='prod_imgs/')
    orderBy = models.FloatField()
    rating = models.CharField(max_length=100)
    src = models.TextField()
    likes = models.IntegerField()
    size = models.CharField(max_length=20)
    quality = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    cast = models.TextField()
    poster = models.ImageField(upload_to='prod_imgs/')

    class Meta:
        ordering = ['-orderBy']

    def get_all_arrivals():
        return NewArrival.objects.all()

    def get_na_by_movie(slug):
        cat_id = MovieCategory.objects.get(slug=slug)
        return NewArrival.objects.filter(movie=cat_id)

    def get_na_by_series(slug):
        cat_id = SeriesCategory.objects.get(slug=slug)
        return NewArrival.objects.filter(series=cat_id)

    def get_na_by_playlist(slug):
        cat_id = PlaylistCategory.objects.get(slug=slug)
        return NewArrival.objects.filter(playlist=cat_id)

    def get_na_by_genre(slug):
        gen_id = Genre.objects.get(slug=slug)
        return NewArrival.objects.filter(genre=gen_id)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('video', args=[self.slug])


class Comment(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True, blank=True)
    playlist_item = models.ForeignKey(Playlist_items, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    newarrival = models.ForeignKey(NewArrival, on_delete=models.CASCADE, null=True, blank=True)
    commentator = models.EmailField()
    body = models.TextField()
    com_name = models.CharField(max_length=128)
    dateAdded = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-dateAdded']

    def get_all_epi_comments(slug):
        ep_id = Episode.objects.get(slug=slug)
        return Comment.objects.filter(episode = ep_id)

    def get_all_pl_comments(slug):
        ep_id = Playlist_items.objects.get(slug=slug)
        return Comment.objects.filter(playlist_item = ep_id)

    def get_all_mv_comments(slug):
        ep_id = Movie.objects.get(slug=slug)
        return Comment.objects.filter(movie = ep_id)

    def get_all_na_comments(slug):
        ep_id = NewArrival.objects.get(slug=slug)
        return Comment.objects.filter(newarrival = ep_id)

    def __str__(self):
        return self.com_name




class SliderCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Slider(models.Model):
    name         = models.CharField(max_length=100)
    category     = models.ForeignKey(SliderCategory, on_delete=models.CASCADE)
    description  = models.TextField()
    img          = models.ImageField(upload_to='prod_imgs/')
    genre        = models.ForeignKey(Genre, on_delete=models.CASCADE)
    quality      = models.CharField(max_length=20)
    watch          = models.URLField()
    release_date = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' | ' + self.category.name + ' | ' + self.genre.name
    

    def get_all_slides():
        return Slider.objects.all()
