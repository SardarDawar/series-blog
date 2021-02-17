import django_filters

from .models import *

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = ['category', 'genre']

class SeriesFilter(django_filters.FilterSet):
    class Meta:
        model = Series
        fields = ['category', 'genre']

class PlaylistFilter(django_filters.FilterSet):
    class Meta:
        model = Playlist
        fields = ['category', 'genre']

class ComingSoonFilter(django_filters.FilterSet):
    class Meta:
        model = ComingSoon
        fields = ['movie', 'series', 'playlist', 'genre']

class NewArrivalFilter(django_filters.FilterSet):
    class Meta:
        model = ComingSoon
        fields = ['movie', 'series', 'playlist', 'genre']