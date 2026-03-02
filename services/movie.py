from typing import Optional

from django.db.models import QuerySet

from db.models import Genre, Actor, Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet[Movie]:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        return Movie.objects.filter(genres__in=genres_ids,
                                    actors__in=actors_ids).distinct()
    if genres_ids:
        return Movie.objects.filter(genres__in=genres_ids)
    if actors_ids:
        return Movie.objects.filter(actors__in=actors_ids)


def get_movie_by_id(id_: int) -> Optional[Movie]:
    return Movie.objects.filter(id=id_).first()


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> Movie:
    film = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        film.genres.add(*genres)
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        film.actors.add(*actors)

    return film
