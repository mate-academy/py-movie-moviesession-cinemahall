from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: list | None = None,
        actors_ids: list | None = None
) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None) -> None:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids is not None:
        movie.genres.add(*genres_ids)

    if actors_ids is not None:
        movie.actors.add(*actors_ids)
