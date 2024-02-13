from django.db.models import QuerySet

from db.models import Movie


def get_movies(
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None,
) -> QuerySet:
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids
        )

    if genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)

    if actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)

    return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None,
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)
