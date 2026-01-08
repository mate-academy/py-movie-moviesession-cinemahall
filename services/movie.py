from django.db.models import QuerySet
from db.models import Movie


def get_movies(
    genres_ids: list[int] = None,
    actors_ids: list[int] = None
) -> QuerySet[Movie] | None:
    if not genres_ids and not actors_ids:
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
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids and isinstance(genres_ids, list):
        movie.genres.add(*genres_ids)
    if actors_ids and isinstance(actors_ids, list):
        movie.actors.add(*actors_ids)
    movie.save()
