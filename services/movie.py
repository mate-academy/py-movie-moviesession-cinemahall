from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list = None,
               actors_ids: list = None) -> QuerySet:

    if genres_ids and actors_ids:
        return Movie.objects.filter(genres__in=genres_ids,
                                    actors__in=actors_ids).distinct()

    elif genres_ids:
        return Movie.objects.filter(genres__in=genres_ids).distinct()
    elif actors_ids:
        return Movie.objects.filter(actors__in=actors_ids).distinct()
    else:
        return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None) -> Movie:
    if genres_ids is None:
        genres_ids = []
    if actors_ids is None:
        actors_ids = []

    movie_obj = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    movie_obj.genres.set(genres_ids)
    movie_obj.actors.set(actors_ids)

    return movie_obj
