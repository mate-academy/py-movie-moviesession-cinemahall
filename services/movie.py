from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list | None = None,
               actors_ids: list | None = None) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    result = Movie.objects.all()
    if genres_ids:
        result = result.filter(genres__id__in=genres_ids)
    if actors_ids:
        result = result.filter(actors__id__in=actors_ids).distinct()
    return result.distinct()


def get_movie_by_id(_id: int) -> Movie:
    return Movie.objects.get(id=_id)


def create_movie(movie_title: str | None = None,
                 movie_description: str | None = None,
                 genres_ids: list | None = None,
                 actors_ids: list | None = None) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
    return new_movie
