from django.urls import path
from music import views

urlpatterns = [
    path('songs/', views.SongsPage, name='songs'),
    path('song/<slug>-ID-<pk>/', views.SingleSongPage, name='single-song'),
    path('song/<slug>-ID-<pk>/like', views.add_favourite, name='add-favourite-song'),
    path('song/<slug>-ID-<pk>/dislike', views.remove_favourite, name='remove-favourite-song'),
    path('news/', views.get_news, name='news'),
]