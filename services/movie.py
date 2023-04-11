from django.db.models import QuerySet

from db.models import Movie
from db.models import Genre
from db.models import Actor


def get_movies(
        genres_ids: list[Genre.pk] = None,
        actors_ids: list[Actor.pk] = None
) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie | None:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[Genre.pk] = None,
        actors_ids: list[Actor.pk] = None
) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids is not None:
        new_movie.genres.set(genres_ids)

    if actors_ids is not None:
        new_movie.actors.set(actors_ids)
