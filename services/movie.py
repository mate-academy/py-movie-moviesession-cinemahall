import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor, Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()
    if genres_ids and not actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids).distinct()
    if actors_ids and not genres_ids:
        return Movie.objects.filter(actors__id__in=actors_ids).distinct()


def get_movie_by_id(movie_id: int) -> QuerySet:
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
