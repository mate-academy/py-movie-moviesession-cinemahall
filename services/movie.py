from typing import List, Optional
from db.models import Movie



def get_movies(
        genres_ids: List[int] = None, actors_ids: List[int] = None
) -> List[Movie]:
    queryset = Movie.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int = None) -> Optional[Movie]:
    query_set = Movie.objects.get(pk=movie_id)

    return query_set


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None,
) -> Movie:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if actors_ids:
        movie.actors.set(actors_ids)
    if genres_ids:
        movie.genres.set(genres_ids)

    return movie
