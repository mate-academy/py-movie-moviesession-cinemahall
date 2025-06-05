from django.db.models import QuerySet
from db.models import Movie


def get_movies(genres_ids: list = None,
               actors_ids: list = None) -> QuerySet[Movie]:
    sett = Movie.objects.all()
    if genres_ids and actors_ids:
        return sett.filter(genres__id__in=genres_ids,
                           actors__id__in=actors_ids)
    if genres_ids:
        return sett.filter(genres__id__in=genres_ids)
    if actors_ids:
        return sett.filter(actors__id__in=actors_ids)
    else:
        return sett
# test commit


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list = None, actors_ids: list = None) -> Movie:
    mm = Movie.objects.create(title=movie_title,
                              description=movie_description)
    if genres_ids:
        mm.genres.add(*genres_ids)
    if actors_ids:
        mm.actors.add(*actors_ids)
