from typing import List
from django.db.models import QuerySet
from db.models import Movie, Genre, Actor


def get_movies(
    genres_ids: List[Genre] = None,
    actors_ids: List[Actor] = None
) -> QuerySet | Movie:
    movies = Movie.objects.all()

    if not genres_ids and not actors_ids:
        return movies
    if genres_ids and actors_ids:
        movies = movies.filter(
            genres__in=genres_ids, actors__in=actors_ids
        )
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
            genre = Genre.objects.get(id=genre_id)
            movie.genres.add(genre)
    if actors_ids:
        for actor_id in actors_ids:
            actor = Actor.objects.get(id=actor_id)
            movie.actors.add(actor)

    movie.save()
