import init_django_orm  # noqa: F401
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from db.models import Movie


def get_movies(
    genres_ids: list[int] = None, actors_ids: list[int] = None
) -> QuerySet[Movie]:
    result = Movie.objects.all()
    if genres_ids is not None:
        result = result.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        result = result.filter(actors__id__in=actors_ids)
    return result


def get_movie_by_id(movie_id: int) -> Movie | None:
    try:
        return Movie.objects.get(id=movie_id)
    except ObjectDoesNotExist:
        print("You provided incorrect ID")
        return None


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] = None,
    actors_ids: list[int] = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description
    )

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
