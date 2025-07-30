from db.models import Movie
from django.db.models.query import QuerySet


def get_movies(
    genres_ids: list[int] = [],
    actors_ids: list[int] = []
) -> QuerySet[Movie]:
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()
    elif genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids).distinct()
    elif actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids).distinct()
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] = [],
    actors_ids: list[int] = []
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
