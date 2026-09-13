from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(genres__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(actors__in=actors_ids)

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> Movie:
    movie = Movie(
        title=movie_title,
        description=movie_description,
    )
    movie.save()

    if genres_ids is not None:
        movie.genres.set(genres_ids)
    if actors_ids is not None:
        movie.actors.set(actors_ids)

    return movie
