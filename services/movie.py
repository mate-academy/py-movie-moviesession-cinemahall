import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list[int] | None = None,
               actors_ids: list[int] | None = None) -> QuerySet:
    query = Movie.objects.all()
    if actors_ids:
        query = query.filter(actors__id__in=actors_ids)
    if genres_ids:
        query = query.filter(genres__id__in=genres_ids)
    return query.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] | None = None,
                 actors_ids: list[int] | None = None) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if actors_ids:
        movie.actors.set(actors_ids)
    if genres_ids:
        movie.genres.set(genres_ids)
