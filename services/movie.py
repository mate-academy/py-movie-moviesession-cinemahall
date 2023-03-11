from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    movie_to_watch = Movie.objects.all()
    if actors_ids is not None:
        movie_to_watch = movie_to_watch.filter(
            actors__id__in=actors_ids
        ).distinct()
    if genres_ids is not None:
        movie_to_watch = movie_to_watch.filter(
            genres__id__in=genres_ids
        ).distinct()
    return movie_to_watch


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.all().get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list = None,
    actors_ids: list = None,
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
