from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> QuerySet:
    query = {
        key: value
        for key, value in [
            ("actors__in", actors_ids),
            ("genres__in", genres_ids)
        ]
        if value is not None
    }

    return Movie.objects.filter(**query).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
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

    if actors_ids is not None:
        movie.actors.set(actors_ids)
    if genres_ids is not None:
        movie.genres.set(genres_ids)
