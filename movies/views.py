from django.views import generic

from .models import Movie


class MoviesList(generic.ListView):
    """List of movies"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(generic.DetailView):

    model = Movie
    slug_field = "url"
