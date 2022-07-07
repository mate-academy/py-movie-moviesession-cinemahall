from typing import List
from db.models import Movie


def get_movies(genres_ids: List[int] = None, actors_ids: List[int] = None):
    queryset = Movie.objects.all()

    if not genres_ids and not actors_ids:
        return queryset

    if genres_ids is not None and actors_ids is not None:
        return queryset.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )

    if genres_ids is not None and not actors_ids:
        return queryset.filter(
            genres__id__in=genres_ids,
        )

    if actors_ids is not None and not genres_ids:
        return queryset.filter(
            actors__id__in=actors_ids,
        )


def get_movie_by_id(movie_id):
    queryset = Movie.objects.all()
    return queryset.get(
        id=movie_id
    )


def create_movie(movie_title,
                 movie_description,
                 genres_ids: List[int] = None,
                 actors_ids: List[int] = None):
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
