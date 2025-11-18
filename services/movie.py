import init_django_orm  # noqa: F401

from django.db.models.query import QuerySet
from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list = [], actors_ids: list = []) -> QuerySet:
    # print(f"Genres_id: {genres_ids} | Actors_id: {actors_ids}")
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
        genres_ids: list = [],
        actors_ids: list = []
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
