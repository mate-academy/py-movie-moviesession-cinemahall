from db.models import Movie
from django.db.models import QuerySet


def get_movies(
    genres_ids: list[int] = None,
    actors_ids: list[int] = None
) -> QuerySet[Movie]:
    movies = Movie.objects.all()
    if actors_ids is not None:
        movies = movies.filter(actors__id__in=actors_ids)
    if genres_ids is not None:
        movies = movies.filter(genres__id__in=genres_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie():
    pass