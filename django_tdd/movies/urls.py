from django.urls import path
from movies.views import MovieListView, MovieSingleView

urlpatterns = [
    path('movies', MovieListView.as_view()),
    path('movies/<pk>', MovieSingleView.as_view())
]