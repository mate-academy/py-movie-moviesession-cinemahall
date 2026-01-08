import init_django_orm  # noqa: F401
from db.models import Movie


def get_movies(genres_ids: list[int] = None, actors_ids: list[int] = None):
    queryset_ = Movie.objects.all()
    if genres_ids and actors_ids:
        queryset_ = queryset_.filter(genres__id__in=genres_ids,
                                     actors__id__in=actors_ids)
        return queryset_
    if genres_ids:
        queryset_ = queryset_.filter(genres__id__in=genres_ids)
        return queryset_
    if actors_ids:
        queryset_ = queryset_.filter(actors__id__in=actors_ids)
        return queryset_
    return queryset_


def get_movie_by_id(movie_id):
    query = Movie.objects.filter(id=movie_id)
    return query.get()


def create_movie(movie_title, movie_description,
                 genres_ids=None,
                 actors_ids=None):
    movie_ = Movie.objects.create(title=movie_title,
                                  description=movie_description)
    if genres_ids:
        movie_.genres.set(genres_ids)
    if actors_ids:
        movie_.actors.set(actors_ids)
    return movie_
