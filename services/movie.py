from django.db.models import QuerySet

from db.models import Movie, Actor, Genre


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet:
    filtered_movie = Movie.objects.all()

    if genres_ids:
        filtered_movie = filtered_movie.filter(genres__id__in=genres_ids)
    if actors_ids:
        filtered_movie = filtered_movie.filter(actors__id__in=actors_ids)
    return filtered_movie


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> None:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genres)
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actors)
