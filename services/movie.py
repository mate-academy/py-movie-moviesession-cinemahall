from db.models import Movie

from django.db.models import QuerySet


def get_movies(
        genres_ids: str = None,
        actors_ids: str = None
) -> QuerySet:
    movies = Movie.objects.all()
    if genres_ids is not None:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: int = None,
        actors_ids: int = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids is not None:
        movie.genres.set(genres_ids)
    if actors_ids is not None:
        movie.actors.set(actors_ids)
    return movie
