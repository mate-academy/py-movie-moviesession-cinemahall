from django.db.models import QuerySet

import init_django_orm  # noqa: F401

from db.models import Movie


def get_movies(
        genres_ids: list | None = None,
        actors_ids: list | None = None
) -> QuerySet[Movie]:

    query = Movie.objects.all()

    if genres_ids and actors_ids:
        query = query.filter(genres__id__in=genres_ids,
                             actors__id__in=actors_ids)
    if genres_ids:
        query = query.filter(genres__id__in=genres_ids)
    if actors_ids:
        query = query.filter(actors__id__in=actors_ids)

    return query


def get_movie_by_id(movie_id: int) -> Movie:
    query = Movie.objects.get(id=movie_id)
    return query


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> Movie:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        for genre_id in genres_ids:
            movie.genres.add(genre_id)
    if actors_ids:
        for actor_id in actors_ids:
            movie.actors.add(actor_id)
    return movie
