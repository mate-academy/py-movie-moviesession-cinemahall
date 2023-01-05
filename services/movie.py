from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    movies = Movie.objects.all()
    if genres_ids is not None:
        movies = movies.filter(genres__in=genres_ids)
    if actors_ids is not None:
        movies = movies.filter(actors__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: list[int] = None,
        genres_ids: list[int] = None,
) -> QuerySet:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if actors_ids:
        new_movie.actors.set(actors_ids)

    if genres_ids:
        new_movie.genres.set(genres_ids)

    return new_movie
