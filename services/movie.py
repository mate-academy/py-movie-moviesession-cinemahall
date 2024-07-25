from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    qset = Movie.objects.all()
    if genres_ids:
        qset = qset.filter(genres_ids)
    if actors_ids:
        qset = qset.filter(actors_ids)
    return qset


def get_movie_by_id(id_: int) -> Movie:
    return Movie.objects.get(id=id_)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        new_movie.genres.add(*genres_ids)
    if actors_ids:
        new_movie.actors.add(*actors_ids)
