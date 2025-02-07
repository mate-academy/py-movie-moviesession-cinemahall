from django.db.models import QuerySet
from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:

    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()

    if actors_ids is None and genres_ids:
        return Movie.objects.filter(genre__in=genres_ids)

    if genres_ids is None and actors_ids:
        return Movie.objects.filter(actor__in=actors_ids)

    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genre__in=genres_ids,
            actor__in=actors_ids
        )


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[str] = None
                 ) -> Movie:
    return Movie.objects.create(
        title=movie_title,
        description=movie_description,
        genres=genres_ids,
        actors=actors_ids
    )
