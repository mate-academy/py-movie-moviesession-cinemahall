from django.db.models import QuerySet
from django.core.exceptions import ObjectDoesNotExist

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie | QuerySet[Movie]:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie | None:
    try:
        return Movie.objects.get(id=movie_id)
    except ObjectDoesNotExist as e:
        print(e)
    except ValueError as e:
        print(e)
    return None


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    obj, created = Movie.objects.get_or_create(
        title=movie_title,
        defaults={"description": movie_description}
    )
    if created:
        if genres_ids:
            obj.genres.set(genres_ids)
        if actors_ids:
            obj.actors.set(actors_ids)
    return obj
