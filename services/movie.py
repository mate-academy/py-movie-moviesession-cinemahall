from typing import List

from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: List[Genre] = None,
        actors_ids: List[Actor] = None
) -> QuerySet:

    if genres_ids and actors_ids:
        movies = Movie.objects.filter(genres__id__in=genres_ids)
        return movies.filter(actors__id__in=actors_ids)
    if actors_ids is None and genres_ids is not None:
        return Movie.objects.filter(genres__id__in=genres_ids)
    if genres_ids is None and actors_ids is not None:
        return Movie.objects.filter(actors__id__in=actors_ids)
    return  Movie.objects.all()

def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)

def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[Genre] = None,
        actors_ids: List[Actor] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
