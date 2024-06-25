from django.db.models import QuerySet
from db.models import Movie


def get_movies(
        genres_ids: list[int],
        actors_ids: list[int] = None
) -> QuerySet:
    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__ids__in=actors_ids)
        return movies


def get_movie_by_id(movies_id: int) -> Movie:
    return Movie.objects.filter(id=movies_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    premier_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        for genre_id in genres_ids:
            premier_movie.gengres.add(genre_id)
    if actors_ids:
        for actor_id in actors_ids:
            premier_movie.actors.add(actor_id)
    return premier_movie
