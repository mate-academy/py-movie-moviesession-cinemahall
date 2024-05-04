from django.db.models import QuerySet, Q

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet[Movie]:
    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = queryset.filter(
            Q(genres__in=genres_ids) & Q(actors__in=actors_ids)
        ).distinct()

    if genres_ids:
        queryset = queryset.filter(genres__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


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
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie
