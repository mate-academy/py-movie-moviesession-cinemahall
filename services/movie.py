from typing import List

from db.models import Movie


def get_movies(genres_ids: List[int] = None, actors_ids: List[int] = None):
    movies_list = Movie.objects.all()

    if actors_ids:
        movies_list = movies_list.filter(actors__id__in=actors_ids)
    if genres_ids:
        movies_list = movies_list.filter(genres__id__in=genres_ids)

    return movies_list


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: List[int] = None, actors_ids: List[int] = None):
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if actors_ids:
        movie.actors.set(actors_ids)
    if genres_ids:
        movie.genres.set(genres_ids)
