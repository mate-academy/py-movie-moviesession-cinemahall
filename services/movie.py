from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list[int] | None = None,
               actors_ids: list[int] | None = None) -> QuerySet:
    qs = Movie.objects.all()

    if genres_ids:
        qs = qs.filter(genres__id__in=genres_ids)
    if actors_ids:
        qs = qs.filter(actors__id__in=actors_ids)
    return qs.distinct()


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: None | list = None,
                 actors_ids: None | list = None) -> Movie:

    new_movie = Movie.objects.create(title=movie_title,
                                     description=movie_description)
    if actors_ids:
        new_movie.actors.set(actors_ids)

    if genres_ids:
        new_movie.genres.set(genres_ids)

    return new_movie
