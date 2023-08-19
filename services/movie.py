from db.models import Movie, Actor, Genre
from typing import List


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> Movie:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()
    if genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids).distinct()

    if actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None) -> Movie:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)
    return movie
