from django.contrib import admin
from .models import *







class MovieCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'genre', 'slug',"time_added","time_updated"]
    prepopulated_fields = {'slug': ('name','category')}
    list_filter = ['category', 'genre']

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'genre', 'slug']
    prepopulated_fields = {'slug': ('name','category')}
    list_filter = ['category', 'genre']


class SeriesCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class PlaylistCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class SeriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'genre', 'slug']
    prepopulated_fields = {'slug': ('name','category')}
    list_filter = ['category', 'genre']

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'series', 'season', 'slug']
    prepopulated_fields = {'slug': ('name', 'series', 'season')}
    list_filter = ['series', 'season']


class PlaylistItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'playlist', 'slug']
    prepopulated_fields = {'slug': ('name', 'playlist')}
    list_filter = ['playlist']

class ComingSoonAdmin(admin.ModelAdmin):
    list_display = ['name', 'movie', 'series', 'playlist', 'genre', 'slug']
    prepopulated_fields = {'slug': ('name', 'movie', 'series', 'playlist')}
    list_filter = ['movie', 'series', 'playlist',]

class NewArrivalAdmin(admin.ModelAdmin):
    list_display = ['name', 'movie', 'series', 'playlist', 'genre', 'slug']
    prepopulated_fields = {'slug': ('name', 'movie', 'series', 'playlist')}
    list_filter = ['movie', 'series', 'playlist',]


class SeasonAdmin(admin.ModelAdmin):
    list_display = ['name', 'series', 'slug']
    prepopulated_fields = {'slug': ('name', 'series')}
    list_filter = ['series']

class CommentAdmin(admin.ModelAdmin):
    list_filter = ['episode']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class SliderAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre', 'category']
    list_filter = ['genre', 'category']

class SliderCatAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(SliderCategory, SliderCatAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(MovieCategory, MovieCategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Episode,EpisodeAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Season,SeasonAdmin)
admin.site.register(Playlist,PlaylistAdmin)
admin.site.register(Playlist_items,PlaylistItemAdmin)
admin.site.register(PlaylistCategory,PlaylistCategoryAdmin)
admin.site.register(ComingSoon,ComingSoonAdmin)
admin.site.register(NewArrival,NewArrivalAdmin)
admin.site.register(Series,SeriesAdmin)
admin.site.register(SeriesCategory,SeriesCategoryAdmin)