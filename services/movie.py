from typing import List
from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: List[Genre] = None,
        actors_ids: List[Actor] = None
) -> List[Movie]:
    queryset = Movie.objects.all()
    if (genres_ids is not None) and (actors_ids is not None):
        queryset = queryset.filter(
            actors__id__in=actors_ids,
            genres__id__in=genres_ids
        )
    elif (genres_ids is None) and (actors_ids is not None):
        queryset = queryset.filter(
            actors__id__in=actors_ids
        )
    elif (genres_ids is not None) and (actors_ids is None):
        queryset = queryset.filter(
            genres__id__in=genres_ids
        )
    return queryset


def get_movie_by_id(movie_id: int) -> str:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[Genre] = None,
        actors_ids: List[Actor] = None
) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)


"""
new_book = Book.objects.create(
        title=title,
        price=price,
        format_id=format_id
    )

    if authors_ids:
        new_book.authors.set(authors_ids)

    return new_book
"""
