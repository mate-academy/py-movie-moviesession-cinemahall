from typing import Optional

from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: Optional[list[int]] = None,
               actors_ids: Optional[list[int]] = None) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie | None:
    return Movie.objects.filter(id=movie_id).first()


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: Optional[list[int]] = None,
                 actors_ids: Optional[list[int]] = None) -> None:
    new_movie = Movie.objects.create(title=movie_title,
                                     description=movie_description)
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
