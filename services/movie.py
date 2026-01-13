from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    elif genres_ids and actors_ids:
        result = Movie.objects.all()
        result = result.filter(genres__id__in=genres_ids)
        result = result.filter(actors__id__in=actors_ids)
        return result.distinct()
    elif genres_ids and not actors_ids:
        result = Movie.objects.all()
        result = result.filter(genres__id__in=genres_ids)
        return result
    elif not genres_ids and actors_ids:
        result = Movie.objects.all()
        result = result.filter(actors__id__in=actors_ids)
    return result


def get_movie_by_id(movie_id: int) -> None | Movie:
    if isinstance(movie_id, int):
        try:
            return Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return None


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None) -> Movie | None:
    result = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        result.genres.set(genres_ids)
    if actors_ids:
        result.actors.set(actors_ids)
    return result
