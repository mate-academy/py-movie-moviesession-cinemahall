from typing import List

from db.models import Movie


def get_movies(genres_ids: List[int] | None = None,
               actors_ids: List[int] | None = None) -> List[Movie]:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    filter_param = {}
    if actors_ids:
        filter_param["actors__id__in"] = actors_ids
    if genres_ids:
        filter_param["genres__id__in"] = genres_ids
    return Movie.objects.filter(**filter_param)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
