from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> QuerySet[Movie]:
    all_movies = Movie.objects.all()
    if genres_ids:
        all_movies = all_movies.filter(genres__in=genres_ids)
    if actors_ids:
        all_movies = all_movies.filter(actors__in=actors_ids)
    return all_movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if actors_ids:
        movie.actors.set(actors_ids)
    if genres_ids:
        movie.genres.set(genres_ids)
    return movie
