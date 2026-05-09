from django.db.models import QuerySet, Q

from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    result = Movie.objects.all()
    query = Q()
    if genres_ids:
        query &= Q(genres__id__in=genres_ids)
    if actors_ids:
        query &= Q(actors__id__in=actors_ids)

    return result.filter(query)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    movie_instance = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie_instance.genres.set(genres_ids)

    if actors_ids:
        movie_instance.actors.set(actors_ids)
