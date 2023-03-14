from typing import List

from db.models import Genre, Movie, Actor


def get_movies(
        genres_ids: List[Genre] = None,
        actors_ids: List[Actor] = None
) -> List[Movie]:
    queryset = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return queryset

    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids
        ).filter(
            actors__id__in=actors_ids
        )
        return queryset

    if genres_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids
        )
        return queryset

    if actors_ids:
        queryset = queryset.filter(
            actors__id__in=actors_ids
        )
        return queryset


def get_movie_by_id(movie_id: int) -> List[Movie]:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None,
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
