from typing import List

from db.models import Genre, Movie


# Retrieve List
def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> List:
    queryset = Genre.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(authors__id__in=actors_ids)

    return queryset


# Retrieve movie
def get_movie_by_id(movie_id: int):
    return Movie.objects.get(movie_id)


# Create
def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> Movie:

    new_movie = Movie.objects.create(
        movie_title=movie_title,
        movie_description=movie_description
    )

    if genres_ids:
        new_movie.movie.set(genres_ids)

    if actors_ids:
        new_movie.movie.set(actors_ids)

    return new_movie
