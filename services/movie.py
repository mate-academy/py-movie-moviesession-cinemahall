from django.db.models import QuerySet

from db.models import Movie, Actor, Genre


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    movie_to_watch = Movie.objects.all()
    if genres_ids is None and actors_ids:
        movie_to_watch = movie_to_watch.filter(
            actors__id__in=actors_ids
        ).distinct()
    if genres_ids and actors_ids is None:
        movie_to_watch = movie_to_watch.filter(
            genres__id__in=genres_ids
        ).distinct()
    if genres_ids and actors_ids:
        movie_to_watch = (
            movie_to_watch.filter(actors__id__in=actors_ids)
            .filter(genres__id__in=genres_ids)
            .distinct()
        )
    return movie_to_watch


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.all().get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list = None,
    actors_ids: list = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        genres = Genre.objects.all().filter(id__in=genres_ids)
        movie.genres.add(*genres)
    if actors_ids:
        actors = Actor.objects.all().filter(id__in=actors_ids)
        movie.actors.add(*actors)
    return movie
