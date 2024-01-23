from db.models import Movie, Genre, Actor
from django.db.models import Model, QuerySet


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        movies = movies.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )
    elif genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    elif actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Model:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    get_movies(genres_ids, actors_ids)

    if genres_ids:
        movie.genres.set(Genre.objects.filter(id__in=genres_ids))

    if actors_ids:
        movie.actors.set(Actor.objects.filter(id__in=actors_ids))

    return movie
