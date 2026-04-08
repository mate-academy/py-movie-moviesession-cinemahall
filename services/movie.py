import init_django_orm  # noqa: F401

from db.models import Movie
from django.db.models.query import QuerySet


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet[Movie]:
    get_query = Movie.objects.all()

    if genres_ids:
        get_query = get_query.filter(genres__id__in=genres_ids)

    if actors_ids:
        get_query = get_query.filter(actors__id__in=actors_ids)

    return get_query


def get_movie_by_id(
        movie_id: int
) -> QuerySet[Movie]:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.add(*genres_ids)

    if actors_ids:
        movie.actors.add(*actors_ids)
