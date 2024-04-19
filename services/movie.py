import init_django_orm  # noqa: F401

from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> Movie:
    filters = {}

    if genres_ids:
        filters["genres__id__in"] = genres_ids

    if actors_ids:
        filters["actors__id__in"] = actors_ids

    return Movie.objects.filter(**filters)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> None:
    movie_data = {
        "title": movie_title,
        "description": movie_description
    }
    new_movie = Movie.objects.create(**movie_data)
    if genres_ids is not None:
        new_movie.genres.set(genres_ids)

    if actors_ids is not None:
        new_movie.actors.set(actors_ids)
