from django.db import transaction
from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None):
    movies = Movie.objects.all()
    if genres_ids and actors_ids:
        movies = movies.filter(genres__id__in=genres_ids, actors__id__in=actors_ids)
    elif genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    elif actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


@transaction.atomic
def create_movie(movie_title: str, movie_description: str, genres_ids: list = None, actors_ids: list = None):
    movie = Movie.objects.create(title=movie_title, description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
