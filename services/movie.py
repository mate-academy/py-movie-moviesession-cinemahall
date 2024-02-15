from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> QuerySet[Movie]:
    movie_all_objects = Movie.objects.all()

    if genres_ids:
        movie_all_objects = movie_all_objects.filter(genres__id__in=genres_ids)

    if actors_ids:
        movie_all_objects = movie_all_objects.filter(actors__id__in=actors_ids)

    return movie_all_objects


def get_movie_by_id(movie_id: int) -> QuerySet[Movie]:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
