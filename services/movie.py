from django.db.models import QuerySet
from db.models import Movie


def get_movies(genres_ids: int,
               actors_ids: int) -> QuerySet | Movie:
    actual_movie = Movie.objects.all()

    if genres_ids:
        actual_movie = actual_movie.filter(genres__id__in=genres_ids)

    if actors_ids:
        actual_movie = actual_movie.filter(actors__id__in=actors_ids)

    return actual_movie.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None) -> Movie:
    add_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        add_movie.genres.set(genres_ids)

    if actors_ids:
        add_movie.actors.set(actors_ids)

    return add_movie
