from db.models import Movie
from django.core.exceptions import ObjectDoesNotExist


def get_movies(genres_ids = None, actors_ids = None):

    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids).distinct()
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids).distinct()
    return queryset

def get_movie_by_id(movie_id):
    try:
        return Movie.objects.get(id=movie_id)
    except ObjectDoesNotExist:
        return None

def create_movie( movie_title, movie_description, actors_ids=None, genres_ids=None):
    movie = Movie.objects.create(title=movie_title, description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
