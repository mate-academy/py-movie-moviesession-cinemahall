from db.models import Movie
from django.db.models.query import QuerySet


def get_movies(
        genres_ids: list | None = None,
        actors_ids: list | None = None) -> QuerySet:
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__in=genres_ids,
            actors__in=actors_ids)
    elif actors_ids and not genres_ids:
        return Movie.objects.filter(actors__in=actors_ids)
    elif genres_ids and not actors_ids:
        return Movie.objects.filter(genres__in=genres_ids)
    return Movie.objects.all()


def get_movie_by_id(id_: int) -> Movie:
    return Movie.objects.get(id=id_)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list | None = None,
                 actors_ids: list | None = None) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)
