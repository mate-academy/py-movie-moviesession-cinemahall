from db.models import Movie, Genre, Actor
from django.db.models.query import QuerySet


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        movies = movies.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()

    elif genres_ids:
        movies = movies.filter(genres__id__in=genres_ids).distinct()

    elif actors_ids:
        movies = movies.filter(actors__id__in=actors_ids).distinct()

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)

    return movie
