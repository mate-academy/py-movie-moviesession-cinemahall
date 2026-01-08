from typing import Optional, List

from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(genres_ids: Optional[List[int]] = None,
               actors_ids: Optional[List[int]] = None) -> QuerySet:
    movies = Movie.objects.all()
    if genres_ids and actors_ids:
        movies = movies.filter(genres__in=genres_ids, actors__in=actors_ids)

    elif genres_ids:
        movies = movies.filter(genres__in=genres_ids)

    elif actors_ids:
        movies = movies.filter(actors__in=actors_ids)

    return movies


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.filter(id=movie_id).get()


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[List[int]] = None,
                 actors_ids: Optional[List[int]] = None) -> QuerySet:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description
    )
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actors)

    return movie
