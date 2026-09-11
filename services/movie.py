from django.db.models import QuerySet
from db.models import Movie, Actor, Genre


def get_movies(
    genres_ids: list[int] | None = None, actors_ids: list[int] | None = None
) -> QuerySet:
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids
        )
    elif genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)
    elif actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)
    else:
        return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None,
) -> Movie:
    movick = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movick.genres.add(*genres)
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movick.actors.add(*actors)
    return movick
