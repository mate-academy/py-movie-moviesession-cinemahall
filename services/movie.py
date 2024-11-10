from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Movie | None:
    return get_object_or_404(Movie, id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
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

    return movie
