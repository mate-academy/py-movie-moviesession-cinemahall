from db.models import Movie
from django.db.models import QuerySet
from typing import Optional


def get_movies(genres_ids: Optional[list[int]] = None,
               actors_ids: Optional[list[int]] = None
               ) -> QuerySet:
    query = Movie.objects.all()
    if genres_ids:
        query = query.filter(genres__id__in=genres_ids)
    if actors_ids:
        query = query.filter(actors__id__in=actors_ids)
    return query


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[list[int]] = None,
                 actors_ids: Optional[list[int]] = None
                 ) -> Movie:
    movie = Movie(
        title=movie_title,
        description=movie_description,
    )
    movie.save()
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    movie.save()
    return movie
