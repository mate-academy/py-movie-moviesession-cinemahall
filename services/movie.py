from django.db.models import QuerySet
from db.models import Movie


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> QuerySet:
    movies = Movie.objects.all()
    if genres_ids and actors_ids:
        movies = movies.filter(
            genres__ids__in=genres_ids,
            actors__ids__in=actors_ids
        )
    elif genres_ids:
        movies = movies.filter(genres__ids__in=genres_ids)
    elif actors_ids:
        movies = movies.filter(actors__ids__in=actors_ids)
    return movies


def get_movies_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None
                 ) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.objects.add(*actors_ids)
