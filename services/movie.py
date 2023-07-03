from typing import Optional

from django.db.models import Q, QuerySet

from db.models import Movie


def get_movies(
        genres_ids: Optional[list] = None,
        actors_ids: Optional[list] = None
        ) -> QuerySet:

    if genres_ids and actors_ids:
        return Movie.objects.filter(
            Q(genres__pk__in=genres_ids)
            & Q(actors__pk__in=actors_ids)
        )

    if genres_ids:
        return Movie.objects.filter(genres__pk__in=genres_ids)

    if actors_ids:
        return Movie.objects.filter(actors__pk__in=actors_ids)

    return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[list] = None,
                 actors_ids: Optional[list] = None
                 ) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)
