from db.models import Movie
from django.db.models import Q, QuerySet
from typing import Optional


def get_movies(
        genres_ids: Optional[list[int]] = None,
        actors_ids: Optional[list[int]] = None
) -> QuerySet[Movie]:

    if genres_ids is not None and actors_ids is not None:
        movies_with_actors = Q(actors__id__in=actors_ids)
        movies_with_genres = Q(genres__id__in=genres_ids)
        return Movie.objects.filter(
            movies_with_actors & movies_with_genres).distinct()
    if genres_ids is not None:
        movies_with_genres = Q(genres__id__in=genres_ids)
        return Movie.objects.filter(movies_with_genres)
    if actors_ids is not None:
        movies_with_actors = Q(actors__id__in=actors_ids)
        return Movie.objects.filter(movies_with_actors)
    return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: Optional[list[int]] = None,
        genres_ids: Optional[list[int]] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)
    if actors_ids is not None:
        movie.actors.set(actors_ids)
    if genres_ids is not None:
        movie.genres.set(genres_ids)
    movie.save()
