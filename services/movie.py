from django.db.models import QuerySet
from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None
               ) -> QuerySet:
    match (genres_ids, actors_ids):
        case (None, None):
            return Movie.objects.all()
        case (_, None):
            return Movie.objects.filter(genres__id__in=genres_ids).distinct()
        case (None, _):
            return Movie.objects.filter(actors__id__in=actors_ids).distinct()
        case _:
            return Movie.objects.filter(
                genres__id__in=genres_ids, actors__id__in=actors_ids
            ).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None
                 ) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
