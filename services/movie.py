from db.models import Movie
from django.db.models.query import QuerySet


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            # __id__in me permite colocar uma lista ou tupla
            genres__id__in=genres_ids, 
            actors__id__in=actors_ids
        )
    elif genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)
    elif actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)

    return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str = None,
        genres_ids: list = None,
        actors_ids: list = None
    ) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

