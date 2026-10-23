from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: int = None,
               actors_ids: int = None
               ) -> QuerySet[Movie]:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    if genres_ids is not None and actors_ids is not None:
        return Movie.objects.filter(genres__id__in=genres_ids,
                                    actors__id__in=actors_ids).distinct()
    if genres_ids is not None and actors_ids is None:
        return Movie.objects.filter(genres__id__in=genres_ids).distinct()
    if actors_ids is not None and genres_ids is None:
        return Movie.objects.filter(actors__id__in=actors_ids).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None) -> Movie:
    film = Movie.objects.create(title=movie_title,
                                description=movie_description)
    if actors_ids is not None:
        film.actors.set(actors_ids)
    if genres_ids is not None:
        film.genres.set(genres_ids)
    return film
