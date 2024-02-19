from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import Movie


def get_movies(
        genres_ids: list | None = None,
        actors_ids: list | None = None
) -> QuerySet:

    movies_query = Movie.objects.all()

    if genres_ids:
        movies_query = movies_query.filter(genres__id__in=genres_ids)

    if actors_ids:
        movies_query = movies_query.filter(actors__id__in=actors_ids)

    return movies_query


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> None:
    new_film = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        new_film.genres.set(genres_ids)

    if actors_ids:
        new_film.actors.set(actors_ids)
