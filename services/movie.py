from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:

    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__in=genres_ids,
            actors__in=actors_ids
        )

    if genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)

    if actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)

    return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)
