from typing import Optional

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: str | None = None,
        actors_ids: str | None = None
) -> str:
    movie = Movie.objects.all()
    if genres_ids:
        movie = movie.filter(
            genres__id__in=genres_ids
        ).distinct()
    if actors_ids:
        movie = movie.filter(
            actors__id__in=actors_ids
        )
    return movie


def get_movie_by_id(movie_id: None) -> Optional[Movie]:
    movie = Movie.objects.get(id=movie_id)
    return movie


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: str = None,
        actors_ids: str = None
) -> None:
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
