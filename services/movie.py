from django.db.models import QuerySet
from db.models import Movie


def get_movie(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        queryset = Movie.objects.filter(
            genres=genres_ids,
            actors=actors_ids
        )
    if genres_ids:
        queryset = queryset.filter(genres=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None) -> Movie:

    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
    return new_movie
