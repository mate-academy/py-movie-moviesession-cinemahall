from typing import Optional

from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(genres_ids = None, actor_ids = None) -> QuerySet[Movie]:
    queryset = Movie.objects.all()

    if genres_ids and actor_ids:
        return queryset.filter(
            genres__id__in=genres_ids,
            actors__id__in=actor_ids
        ).distinct()
    elif genres_ids:
        return queryset.filter(
            genres__id__in=genres_ids
        ).distinct()
    elif actor_ids:
        return queryset.filter(
            actors__id__in=actor_ids
        ).distinct()
    else:
        return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str = None,
        genres_ids: Optional[list[int]] = None,
        actor_ids: Optional[list[int]] = None) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actor_ids:
        actors = Actor.objects.filter(id__in=actor_ids)
        movie.actors.set(actors)

    return movie
