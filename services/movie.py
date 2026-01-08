from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None) -> QuerySet:

    query_set = Movie.objects.all()
    if genres_ids:
        query_set = query_set.filter(genres__id__in=genres_ids)
    if actors_ids:
        query_set = query_set.filter(actors__id__in=actors_ids)
    return query_set


def get_movie_by_id(id_db: int) -> Movie | None :
    return Movie.objects.filter(id=id_db).first()


def create_movie(movie_title: str = None,
                 movie_description: str = None,
                 genres_ids: list = None,
                 actors_ids: list = None) -> Movie:

    inst = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if inst and genres_ids:
        inst.genres.set(genres_ids)
    if inst and actors_ids:
        inst.actors.set(actors_ids)

    return inst
