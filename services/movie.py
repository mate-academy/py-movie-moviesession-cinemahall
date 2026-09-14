from django.db.models import QuerySet
from db.models import Movie


def get_movies(
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None,
) -> QuerySet:
    filters = {}

    if genres_ids:
        filters["genres__id__in"] = genres_ids

    if actors_ids:
        filters["actors__id__in"] = actors_ids

    return Movie.objects.filter(**filters)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None,
) -> Movie:
    film = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        film.genres.set(genres_ids)

    if actors_ids:
        film.actors.set(actors_ids)
    return film
