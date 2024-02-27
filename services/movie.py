from typing import List
from django.db.models import QuerySet
from db.models import Movie, Genre, Actor


def get_movies(
    genres_ids: List[Genre] = None,
    actors_ids: List[Actor] = None
) -> QuerySet | Movie:
    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genres__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str, movie_description: str,
        genres_ids: List[int] = None, actors_ids: List[int] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        for genre_id in genres_ids:
            movie.genres.set([genre_id])
    if actors_ids:
        for actor_id in actors_ids:
            movie.actors.set([actor_id])

    movie.save()
