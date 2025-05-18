from db.models import Movie, Genre, Actor
from typing import Optional


def get_movies(genres_ids: list, actors_ids: list) -> None:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    elif genres_ids is not None and actors_ids is not None:
        return Movie.objects.filter(
            genre__id__in=genres_ids,
            actor__id__in=actors_ids
        )
    elif genres_ids is not None:
        return Movie.objects.filter(
            genre__id__in=genres_ids
        ).distinct()
    if actors_ids is not None:
        return Movie.objects.filter(
            actor__id__in=actors_ids
        ).distinct()


def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        print("Movie doesn't exist")
        return None


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list = None, actors_ids: list = None, ) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genres)
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actors)
