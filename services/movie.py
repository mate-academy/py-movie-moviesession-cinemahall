from django.db.models.query import QuerySet

from db.models import Movie

def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        movies = movies.filter(genres__id__in=genres_ids, actors__id__in=actors_ids)
    elif genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    elif actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)

    return movies.distinct()