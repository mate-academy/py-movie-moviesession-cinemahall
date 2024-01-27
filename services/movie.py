from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_id: list[int] = None
) -> QuerySet:

    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_id:
        queryset = queryset.filter(actors__id__in=actors_id)

    return queryset


def get_movie_by_id(
        movie_id: id
) -> QuerySet:
    return Movie.object.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:

    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.set(
            genres_ids
        )

    if actors_ids:
        new_movie.set(
            actors_ids
        )

    return new_movie
