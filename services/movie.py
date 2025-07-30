from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> QuerySet:

    movie_query = Movie.objects.all()

    if genres_ids:
        movie_query = movie_query.filter(genres__id__in=genres_ids)
    if actors_ids:
        movie_query = movie_query.filter(actors__id__in=actors_ids)

    return movie_query


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: list = None,
        genres_ids: list = None
) -> None:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if actors_ids:
        movie.actors.set(actors_ids)
    if genres_ids:
        movie.genres.set(genres_ids)
