from django.contrib.sitemaps import Sitemap
from django.urls.base import reverse
from .models import ComingSoon, Episode, Movie, NewArrival, Playlist, Playlist_items, Season, Series




class PagesSiteMap(Sitemap):

    def items(self):
        return ['home', 'movie', 'series', 'playlist', 'newarrival', 'comingsoon']
    def location(self, item):
        return reverse(item)



class MovieSiteMap(Sitemap):

    def items(self):
        return Movie.objects.all()

class SeriesSiteMap(Sitemap):

    def items(self):
        return Series.objects.all()

class PlaylistSiteMap(Sitemap):

    def items(self):
        return Playlist.objects.all()


class NewArrivalSiteMap(Sitemap):

    def items(self):
        return NewArrival.objects.all()

class SeasonSiteMap(Sitemap):

    def items(self):
        return Season.objects.all()

class EpisodeSiteMap(Sitemap):

    def items(self):
        return Episode.objects.all()

class PlaylistItemSiteMap(Sitemap):

    def items(self):
        return Playlist_items.objects.all()