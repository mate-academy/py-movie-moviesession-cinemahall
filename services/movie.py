import init_django_orm  # noqa: F401

from django.db.models.query import QuerySet
from db.models import Movie


def get_movies(
        genres_ids: list | None = None,
        actors_ids: list | None = None
) -> QuerySet:
    if not genres_ids and not actors_ids:
        movies = Movie.objects.all()
    if not genres_ids and actors_ids:
        movies = Movie.objects.filter(actors__in=actors_ids).distinct()
    if genres_ids and not actors_ids:
        movies = Movie.objects.filter(genres__in=genres_ids).distinct()
    if genres_ids and actors_ids:
        movies = Movie.objects.filter(
            genres__in=genres_ids,
            actors__in=actors_ids
        ).distinct()
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list | None = None,
        actors_ids: list | None = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
