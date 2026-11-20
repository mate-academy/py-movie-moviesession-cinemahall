from django.db.models import QuerySet
from db.models import Movie

def get_movies(
    genres_ids: list[int] = None,
    actors_ids: list[int] = None
) -> QuerySet[Movie]:
    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies.distinct()

def get_movie_by_id():
    pass


def create_movie():
    pass