from django.db.models import QuerySet, Q

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    movie_filters = Q()

    if genres_ids:
        movie_filters &= Q(genres__in=genres_ids)

    if actors_ids:
        movie_filters &= Q(actors__in=actors_ids)

    return Movie.objects.filter(movie_filters)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        movie_description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

