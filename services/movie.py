from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    queryset = Movie.objects.all()

    if not genres_ids and not actors_ids:
        return queryset

    if genres_ids and actors_ids:
        queryset = queryset.filter(genres__in=genres_ids)
        queryset = queryset.filter(actors__in=actors_ids)

    if genres_ids and not actors_ids:
        queryset = queryset.filter(genres__in=genres_ids)

    if actors_ids and not genres_ids:
        queryset = queryset.filter(actors__in=actors_ids)

    return queryset

def get_movie_by_id():
    ...

def create_movie():
    ...