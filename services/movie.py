from typing import List

from db.models import Genre, Actor, Movie


def get_movies(genres_ids: List[int] | None = None,
               actors_ids: List[int] | None = None) -> List[Movie]:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids,
                                    genres__id__in=genres_ids)
    if genres_ids and not actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)
    if actors_ids and not genres_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[Genre] = None,
        actors_ids: List[Actor] = None) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
