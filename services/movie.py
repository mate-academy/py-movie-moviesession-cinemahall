from typing import List
from db.models import Movie


def get_movies(genres_ids: List[int] = None, actors_ids: List[int] = None):
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id):
    return Movie.objects.get(pk=movie_id)


def create_movie(movie_title,
                 movie_description,
                 genres_ids: List[int] = None,
                 actors_ids: List[int] = None
                 ):

    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description
                                 )
    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)
