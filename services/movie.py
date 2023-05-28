from typing import Optional

from db.models import Movie


def get_movies(
    genres_ids: Optional[list[int]] = None,
    actors_ids: Optional[list[int]] = None,
) -> Optional[list[Movie]]:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    if genres_ids is not None and actors_ids is not None:
        return Movie.objects.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids
        )
    if genres_ids is not None:
        return Movie.objects.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        return Movie.objects.filter(actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[list[int]] = None,
    actors_ids: Optional[list[int]] = None,
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids is not None:
        movie.genres.set(genres_ids)
    if actors_ids is not None:
        movie.actors.set(actors_ids)
