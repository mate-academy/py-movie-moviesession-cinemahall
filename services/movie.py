from db.models import Movie, Genre, Actor
from typing import Optional, List


def get_movies(genres_ids: Optional[List[int]] = None,
               actors_ids: Optional[List[int]] = None
               ) -> Movie:
    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = queryset.filter(genres__id__in=genres_ids,
                                   actors__id__in=actors_ids)
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: Optional[List[int]] = None,
                 actors_ids: Optional[List[int]] = None
                 ) -> Movie:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description)

    if genres_ids:
        movie.genres.set(Genre.objects.filter(id__in=genres_ids))
    if actors_ids:
        movie.actors.set(Actor.objects.filter(id__in=actors_ids))

    return movie
