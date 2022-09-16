from django.urls import path

from django.conf.urls.static import static          #lib needs to open image
from django.conf import settings                    #lib needs to open image

from . import views

urlpatterns = [
    path('cinemas/', views.CinemasView.as_view()),
    path('cinemas/<int:pk>/', views.CinemasDetailView.as_view()),
    path('movies/', views.MovieView.as_view()),
    path('movies/<int:pk>/', views.MovieDetailView.as_view()),
    path('show-times/', views.ShowTimeView.as_view()),
    path('show-times/<int:pk>/', views.ShowTimeDetailView.as_view()),
    path('rooms/', views.RoomsView.as_view()),
    path('rooms/<int:pk>/', views.RoomsDetailView.as_view()),
    path('rooms-format/', views.RoomsFormatView.as_view()),
    path('rooms-format/<int:pk>/', views.RoomsFormatDetailView.as_view()),
    path('movie_categories/', views.CategoryView.as_view({'get': 'list',})),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)