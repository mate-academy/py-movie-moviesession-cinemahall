from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None
               ) -> QuerySet:
    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None
                 ) -> None:
    result_of_movie = Movie.objects.create(title=movie_title,
                                           description=movie_description,
                                           )
    if actors_ids:
        result_of_movie.actors.set(actors_ids)

    if genres_ids:
        result_of_movie.genres.set(genres_ids)
