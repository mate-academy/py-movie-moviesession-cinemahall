from typing import List

from django.db.models import QuerySet

from db.models import Movie, Actor, Genre


def get_movies(genres_ids: List[Genre] = None,
               actors_ids: List[Actor] = None) -> QuerySet:
    if genres_ids and actors_ids:
        return_movie = Movie.objects.filter(genres_ids)
        return_movie = return_movie.filter(actors_ids)
        return return_movie

    if genres_ids:
        return Movie.objects.filter(genres_ids)

    if actors_ids:
        return Movie.objects.filter(actors_ids)

    return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: List[int],
                 actors_ids: List[int]) -> None:
    Movie.objects.create(title=movie_title,
                         description=movie_description,
                         actors=actors_ids,
                         genres=genres_ids)
