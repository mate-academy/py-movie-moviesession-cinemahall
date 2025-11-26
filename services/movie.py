from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.genres__id__in = genres_ids
    if actors_ids:
        queryset = queryset.actors__id__in = actors_ids
    return queryset.distinct()


def get_movie_by_id(id_: int) -> Movie | None:
    return Movie.objects.get(id=id_)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list = None, actors_ids: list = None) -> None:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
