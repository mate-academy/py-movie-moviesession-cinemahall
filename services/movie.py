from django.db.models import QuerySet
from db.models import Movie


def get_movies(
        genres_ids: list[int], actors_ids: list[int]
        ) -> QuerySet[Movie] | None:
    if not genres_ids or not actors_ids:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )
    if genres_ids and not actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)
    if not genres_ids and actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie | None:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int],
        actors_ids: list[int]
) -> None:
    Movie.objects.create(
        title=movie_title,
        description=movie_description,
        genres_id=genres_ids,
        actors_id=actors_ids
    )