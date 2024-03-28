from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None) -> QuerySet:
    movie = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return movie
    if genres_ids and actors_ids:
        movie = movie.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids).distinct()
    elif genres_ids:
        movie = movie.filter(genres__id__in=genres_ids).distinct()
    elif actors_ids:
        movie = movie.filter(actors__id__in=actors_ids)
    return movie


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None) -> QuerySet:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)
    return movie
