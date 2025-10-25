from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    qs = Movie.objects.all()
    if genres_ids:
        qs = qs.filter(genres__id__in=genres_ids)
    if actors_ids:
        qs = qs.filter(actors__id__in=actors_ids)
    return qs.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
) -> Movie:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.create(
            title=movie_title,
            description=movie_description
        )
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if isinstance(genres_ids, (list, tuple)):
        movie.genres.set(genres_ids)
    else:
        genres_ids = [genres_ids]
        movie.genres.set(genres_ids)

    if isinstance(actors_ids, (list, tuple)):
        movie.actors.set(actors_ids)
    else:
        actors_ids = [actors_ids]
        movie.actors.set(actors_ids)

    return movie
