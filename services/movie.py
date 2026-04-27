from typing import List

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet[Movie] | Movie:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids,
        )
    if actors_ids is None:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
        )

    if genres_ids is None:
        return Movie.objects.filter(
            actors__id__in=actors_ids,
        )


def get_movie_by_id(
        movie_id: int = None
) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str = None,
        movie_description: str = None,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None,
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if actors_ids:
        new_movie.actors.set(actors_ids)

    if genres_ids:
        new_movie.genres.set(genres_ids)
