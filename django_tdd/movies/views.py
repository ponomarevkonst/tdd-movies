from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieListView(ListAPIView, CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

