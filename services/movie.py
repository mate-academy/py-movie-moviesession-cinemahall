from db.models import Movie, Actor, Genre
from django.db.models import QuerySet


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None) -> QuerySet[Movie]:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids)
    if genres_ids and not actors_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids and not genres_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: list[int] = None,
        genres_ids: list[int] = None) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)
    if actors_ids:
        movie.actors.set(Actor.objects.filter(id__in=actors_ids))
    if genres_ids:
        movie.genres.set(Genre.objects.filter(id__in=genres_ids))
    return movie
