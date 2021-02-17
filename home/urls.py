from django.conf.urls import handler404, handler500, url
from django.urls import path
from .views import *



urlpatterns = [
        path('', homeView, name= 'home'),
        path('autocomp', autocomp, name = 'autocomp'),
        path('movieprofile/<str:slug>', movieProfile, name= 'movieprofile'),
        path('epi/<str:slug>', episodeView, name= 'epi'),
        path('video/<str:slug>', Video, name= 'video'),
        path('comment/<str:slug>', CommentView, name= 'comment'),
        path('clearsession/', clearSession, name= 'clearsession'),
        path('like_ep', likeEp, name= 'like_ep'),


        path('moviefilter/<str:slug>', movieFilter, name= 'moviefilter'),
        path('seriesfilter/<str:slug>', seriesFilter, name= 'seriesfilter'),
        path('playfilter/<str:slug>', playlistFilter, name= 'playfilter'),
        path('nafilter/<str:slug>', newArrFilter, name= 'nafilter'),
        path('csfilter/<str:slug>', comingSoonFilter, name= 'csfilter'),

        path('detail/<str:slug>', detail, name= 'detail'),

        path('movie/', movie, name= 'movie'),
        path('series/', series, name= 'series'),
        path('playlist/', playlist, name= 'playlist'),
        path('comingsoon/', comingSoon, name= 'comingsoon'),
        path('newarrival/', newArrival, name= 'newarrival'),


        path('clearsession/', clearSession, name= 'clearsession'),
]

