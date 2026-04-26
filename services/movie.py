from typing import Optional, List
from django.db.models import QuerySet
from db.models import Movie, Genre, Actor


def get_movies(
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None,
) -> QuerySet[Movie]:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    elif genres_ids is not None and actors_ids is not None:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids,
        )
    elif genres_ids is not None:
        return Movie.objects.filter(genres__id__in=genres_ids)
    elif actors_ids is not None:
        return Movie.objects.filter(actors__id__in=actors_ids)
    return Movie.objects.none()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids is not None:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genres)
    if actors_ids is not None:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actors)
    return movie
