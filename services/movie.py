from django.db.models import QuerySet
from db.models import Movie
from django.db.models import Q


def get_movies(
    genres_ids: list[int] = None,
    actors_ids: list[int] = None
) -> QuerySet[Movie]:
    query = Q()
    if genres_ids:
        query &= Q(genres__in=genres_ids)
    if actors_ids:
        query &= Q(actors__in=actors_ids)
    return Movie.objects.filter(query).prefetch_related("actors", "genres")


def get_movie_by_id(movie_id: int) -> Movie | None:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] = None,
    actors_ids: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
