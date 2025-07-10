from typing import Optional

from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: Optional[list] = None,
               actors_ids: Optional[list] = None) -> (QuerySet[Movie]
                                                      | None):
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()

    if genres_ids is not None and actors_ids is not None:
        movies = Movie.objects.filter(genres__in=genres_ids)
        return movies.filter(actors__in=actors_ids).distinct()

    if genres_ids is not None and actors_ids is None:
        return Movie.objects.filter(genres__in=genres_ids)

    if genres_ids is None and actors_ids is not None:
        return Movie.objects.filter(actors__in=actors_ids)

    return None


def get_movie_by_id(movie_id: int) -> QuerySet[Movie] | None:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[list] = None,
                 actors_ids: Optional[list] = None) -> (QuerySet[Movie]
                                                        | None):

    movie = Movie.objects.get_or_create(title=movie_title,
                                        description=movie_description)
    if genres_ids is not None:
        movie[0].genres.set(genres_ids)
    if actors_ids is not None:
        movie[0].actors.set(actors_ids)
    return movie
