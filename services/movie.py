from django.db.models import QuerySet

from db.models import Movie


def get_movies(
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None
) -> QuerySet[Movie] | Movie:

    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors__in=actors_ids)

    return queryset
    pass


def get_movie_by_id(
    movie_id: int | None = None
) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)
    pass
