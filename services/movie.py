from django.db.models import QuerySet
from db.models import Movie

from services.serv_support import all_ints


def get_movies(genres_ids: list[int] | None = None,
               actors_ids: list[int] | None = None) -> QuerySet:
    query = Movie.objects.all()
    if all_ints(genres_ids):
        query = query.filter(genres__id__in=genres_ids)
    if all_ints(actors_ids):
        query = query.filter(actors__id__in=actors_ids)
    return query


def get_movie_by_id(movie_id=int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list[int] | None = None,
                 actors_ids: list[int] | None = None) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if all_ints(actors_ids):
        new_movie.actors.set(actors_ids)

    if all_ints(genres_ids):
        new_movie.genres.set(genres_ids)
    return new_movie
