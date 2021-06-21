from django.urls import path

from . import views


urlpatterns = [
    path('', views.MoviesList.as_view()),
    path('filter/', views.FilterMovieView.as_view(), name='filter'),
    path('search/', views.Search.as_view(), name='search'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('actor/<str:slug>/', views.ActorView.as_view(), name='actor_detail'),

]
