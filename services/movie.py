from django.db.models import QuerySet

from django.db.models import Q

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list | None = None,
        actors_ids: list | None = None
) -> QuerySet[Movie]:
    query = Q()
    if genres_ids:
        query &= Q(genres__id__in=genres_ids)
    if actors_ids:
        query &= Q(actors__id__in=actors_ids)
    return Movie.objects.filter(query)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list | None = None,
    actors_ids: list | None = None
) -> Movie:

    movie = Movie.objects.create(
        title=movie_title, description=movie_description)
    if genres_ids:
        movie.genres.set(Genre.objects.filter(id__in=genres_ids))
    if actors_ids:
        movie.actors.set(Actor.objects.filter(id__in=actors_ids))
    return movie
