from db.models import Movie, Genre, Actor
from typing import List, Optional


def get_movies(genres_ids: Optional[List[int]] = None,
               actors_ids: Optional[List[int]] = None) -> None:
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids).distinct()

    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids).distinct()

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    movie = Movie.objects.get(id=movie_id)
    return movie


def create_movie(movie_title: str,
                 movie_description: str,
                 actors_ids: Optional[List[int]] = None,
                 genres_ids: Optional[List[int]] = None) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)

    return movie
