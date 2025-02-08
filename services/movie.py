# movie.py

from django.db.models import QuerySet
from db.models import Movie, Genre, Actor


def get_movies(
    genres_ids: list[int] = None,
    actors_ids: list[int] = None
) -> QuerySet:
    """_summary_
    -   get_movies, takes optional genres_ids - a list of genres ids, optional
        actors_ids - a list of actors ids.

        -   If genres_ids and actors_ids are not provided, the method returns
            all movies
        - If both genres_ids and actors_ids are provided, the method returns
            movies, that have at least one genre from genres_ids and one actor
            from actors_ids.
        -   If only genres_ids is provided, the method returns the queryset
            with movies, that have at least one genre from genres_ids
        -   If only actors_ids is provided, the method returns the queryset
            with movies, that have at least one actor from actors_ids

    Args:
        genres_ids (list[int], optional): _description_. Defaults to None.
        actors_ids (list[int], optional): _description_. Defaults to None.

    Returns:
        QuerySet: _description_
    """
    query_movies = Movie.objects.all()

    if genres_ids and actors_ids:
        return query_movies.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )
    elif genres_ids:
        return query_movies.filter(
            genres__id__in=genres_ids
        )
    elif actors_ids:
        return query_movies.filter(
            actors__id__in=actors_ids
        )

    return query_movies.distinct()


def get_movie_by_id(
    movie_id: int
) -> Movie:
    """_summary_
    -   get_movie_by_id, takes movie_id - id of the movie, returns movie with
        the provided id.

    Args:
        movie_id (int): _description_

    Returns:
        Movie: _description_
    """
    return Movie.objects.get(
        id=movie_id
    )


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] = None,
    actors_ids: list[int] = None
) -> Movie:
    """_summary_
    -   create_movie, takes movie_title, movie_description, optional
        genres_ids and optional actors_ids, genres_ids and actors_ids are the
        list of genres ids and the list of actors ids respectively, method
        creates movie with provided title and description, add him genres if
        genres_ids is provided, add him actors if actors_ids is provided.

    Args:
        movie_title (str): _description_
        movie_description (str): _description_
        genres_ids (list[int], optional): _description_. Defaults to None.
        actors_ids (list[int], optional): _description_. Defaults to None.

    Returns:
        Movie: _description_
    """
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if actors_ids:
        new_movie.actors.set(
            Actor.objects.filter(
                id__in=actors_ids
            )
        )
    if genres_ids:
        new_movie.genres.set(
            Genre.objects.filter(
                id__in=genres_ids
            )
        )

    new_movie.save()

    return new_movie
