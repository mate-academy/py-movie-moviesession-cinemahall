from django.db.models import QuerySet, Q

from db.models import Movie


def get_movies(
    genres_ids: list[int] = None, actors_ids: list[int] = None
) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if not actors_ids:
        return Movie.objects.filter(genres__in=genres_ids)

    if not genres_ids:
        return Movie.objects.filter(actors__in=actors_ids)

    return Movie.objects.filter(
        Q(genres__in=genres_ids) & Q(actors__in=actors_ids)
    )


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] = None,
    actors_ids: list[int] = None,
) -> Movie:

    new_movie = Movie(title=movie_title, description=movie_description)
    new_movie.save()
    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
    new_movie.save()

    return new_movie
