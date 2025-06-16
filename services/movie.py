from typing import Optional, List
from django.db.models.query import QuerySet
from db.models import Movie


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> QuerySet:
    qs = Movie.objects.all()

    if genres_ids and actors_ids:
        qs = qs.filter(genres__id__in=genres_ids,
                       actors__id__in=actors_ids).distinct()
    elif genres_ids:
        qs = qs.filter(genres__id__in=genres_ids).distinct()
    elif actors_ids:
        qs = qs.filter(actors__id__in=actors_ids).distinct()

    return qs


def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    return Movie.objects.filter(id=movie_id).first()


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: int = None,
        actors_ids: int = None) -> Optional[Movie]:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
