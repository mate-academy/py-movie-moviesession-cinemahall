from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None,
) -> QuerySet:

    if not genres_ids and not actors_ids:
        return Movie.objects.all()
