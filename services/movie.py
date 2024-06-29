import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor, Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    movie = Movie.objects.all()
    if genres_ids:
        movie = movie.filter(genres__in=genres_ids)
    if actors_ids:
        movie = movie.filter(actors__in=actors_ids)
    return movie


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None,
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)
