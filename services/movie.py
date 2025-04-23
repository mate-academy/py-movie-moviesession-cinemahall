# from django.db.models import QuerySet, Manager
from typing import Optional, Any
from db.models import Movie


def get_movies(genres_ids: Optional[list[int]] = None,
               actors_ids: Optional[list[int]] = None) -> Any:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()
    if genres_ids and not actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids).distinct()
    if actors_ids and not genres_ids:
        return Movie.objects.filter(actors__id__in=actors_ids).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[list[int]] = None,
                 actors_ids: Optional[list[int]] = None,
                 ) -> Movie:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description, )
    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
