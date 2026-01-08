from typing import Optional
from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None) -> QuerySet[Movie]:
    qs = Movie.objects.all()

    if genres_ids and actors_ids:
        qs = qs.filter(genres__id__in=genres_ids, actors__id__in=actors_ids)
    elif genres_ids:
        qs = qs.filter(genres__id__in=genres_ids)
    elif actors_ids:
        qs = qs.filter(actors__id__in=actors_ids)

    return qs.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: Optional[list[int]] = None,
                 actors_ids: Optional[list[int]] = None) -> Movie:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description)

    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie


def update_movie(movie_id: int, movie_title: str = None,
                 movie_description: str = None,
                 genres_ids: Optional[list[int]] = None,
                 actors_ids: Optional[list[int]] = None) -> Movie:
    movie = Movie.objects.get(id=movie_id)

    if movie_title:
        movie.title = movie_title
    if movie_description:
        movie.description = movie_description

    movie.save()

    if genres_ids is not None:
        movie.genres.set(genres_ids)
    if actors_ids is not None:
        movie.actors.set(actors_ids)

    return movie
