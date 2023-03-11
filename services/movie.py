from django.db.models import Q
from django.db.models.query import QuerySet

from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet[Movie]:
    movies = Movie.objects.all()
    filter_kwargs = {}

    if genres_ids:
        filter_kwargs["genres__id__in"] = genres_ids
    if actors_ids:
        filter_kwargs["actors__id__in"] = actors_ids

    if filter_kwargs:
        filter_q = Q(**filter_kwargs)
        movies = movies.filter(filter_q).distinct()

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)
