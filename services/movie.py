import init_django_orm  # noqa: F401
from django.db.models import QuerySet

from db.models import Genre, Actor, Movie


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> QuerySet:
    movies = Movie.objects.all()
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    return movies.distinct()


def get_movie_by_id(movie_id: int) -> type(object):
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> type(object):
    new_movie = Movie.objects.filter(title=movie_title).first()
    if not new_movie:
        new_movie = Movie(title=movie_title, description=movie_description)
        new_movie.save()
    if genres_ids:
        genres_set = Genre.objects.filter(id__in=genres_ids)
        new_movie.genres.add(*genres_set)
    if actors_ids:
        actors_set = Actor.objects.filter(id__in=actors_ids)
        new_movie.actors.add(*actors_set)
    del new_movie
