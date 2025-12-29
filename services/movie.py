from typing import List, Optional

from django.db.models.query import QuerySet

from db.models import Movie


def get_movies(genres_ids: Optional[List[int]] = None,
               actors_ids: Optional[List[int]] = None) -> QuerySet:
    result_query = Movie.objects.all()

    if genres_ids:
        result_query = result_query.filter(genres__id__in=genres_ids)

    if actors_ids:
        result_query = result_query.filter(actors__id__in=actors_ids)

    return result_query


def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[List[int]] = None,
                 actors_ids: Optional[List[int]] = None) -> None:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
