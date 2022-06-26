from typing import List
from db.models import Movie, Genre, Actor


def get_movies(genres_ids: List[int] = None, actors_ids: List[int] = None):
    queryset = Movie.objects.all()
    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(search_id):
    queryset = Movie.objects.get(id=search_id)
    return queryset


def create_movie(
        movie_title,
        movie_description,
        genres_ids: List[Genre] = None,
        actors_ids: List[Actor] = None):
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
