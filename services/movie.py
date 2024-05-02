from django.db.models import QuerySet

from db.models import Movie


def get_movies(
    genres_ids: list[int] = None,
    actors_ids: list[int] = None
) -> QuerySet[Movie]:

    queryset = Movie.objects.all()

    if genres_ids:
        queryset.filter(genres__movie__in=genres_ids)
    if actors_ids:
        queryset.filter(actors__movie__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] = None,
    actors_ids: list[int] = None
) -> None:

    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        new_movie = Movie.genres.set(genres_ids)
    if actors_ids:
        new_movie = Movie.actors.set(actors_ids)

    return new_movie
