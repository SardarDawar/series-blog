from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from . import settings
from home.sitemaps import *

sitemaps = {
    'pages': PagesSiteMap,
    'movies': MovieSiteMap,
    'series': SeriesSiteMap,
    'playlists': PlaylistSiteMap,
    'new_arrivals': NewArrivalSiteMap,
    'seasons': SeasonSiteMap,
    'episode': EpisodeSiteMap,
    'playlistitem': PlaylistItemSiteMap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


handler404 = 'home.views.error_404_view'
handler500 = 'home.views.error_500_view'