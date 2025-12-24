from typing import Optional

from django.db.models.query import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: Optional[list] = None,
        actors_ids: Optional[list] = None
) -> QuerySet[Movie]:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> QuerySet[Movie]:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[list] = None,
        actors_ids: Optional[list] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description
    )

    if genres_ids:
        movie.genres.add(*Genre.objects.filter(id__in=genres_ids))

    if actors_ids:
        movie.actors.add(*Actor.objects.filter(id__in=actors_ids))

    movie.save()
