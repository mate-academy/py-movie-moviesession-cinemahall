from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list[int] | None = None,
               actors_ids: list[int] | None = None
               ) -> QuerySet:
    movies = Movie.objects.all()

    if actors_ids:
        movies = Movie.objects.filter(
            actors__id__in=actors_ids
        )

    if genres_ids:
        movies = Movie.objects.filter(
            genres__id__in=genres_ids,
        )

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None
                 ) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
