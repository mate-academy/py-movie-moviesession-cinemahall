from django.db.models import QuerySet
from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids).distinct()
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids).distinct()
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list = None, actors_ids: list = None)\
        -> QuerySet | Movie:
    queryset = Movie.objects.create(title=movie_title,
                                    description=movie_description)
    if genres_ids:
        queryset.genres.add(*genres_ids)
    if actors_ids:
        queryset.actors.add(*actors_ids)
    return queryset
