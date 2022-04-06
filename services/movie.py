from typing import List

from db.models import Movie


# Retrieve List
def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> List:
    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(authors__id__in=actors_ids)

    return queryset


# Retrieve movie
def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


# Create
def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
):

    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
