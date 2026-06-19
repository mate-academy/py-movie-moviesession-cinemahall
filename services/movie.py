import warnings
from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(
            genres__in=genres_ids
        )
    if actors_ids:
        queryset = queryset.filter(
            actors__in=actors_ids
        )

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    if not movie_id:
        warnings.warn("You dont specify movie_id")
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: list[int] = None,
        genres_ids: list[int] = None,
) -> Movie:
    if not (movie_title or movie_description):
        warnings.warn(
            "You dont specify movie_title or movie_description"
        )
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if actors_ids:
        movie.actors.set(actors_ids)
    if genres_ids:
        movie.genres.set(genres_ids)
    return movie
