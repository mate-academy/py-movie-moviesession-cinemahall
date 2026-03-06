from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )
    elif genres_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids
        )
    elif actors_ids:
        queryset = queryset.filter(
            actors__id__in=actors_ids
        )

    return queryset


def get_movie_by_id(movie_id):
    return Movie.objects.get(movie_id=movie_id)


def create_movie(movie_title= None, movie_description = None,
                 genres_ids = None, actors_ids = None) -> QuerySet|Movie:
    create = Movie.objects.create(title=movie_title, description=movie_description)

    if genres_ids:
        Movie.genres.set(genres_ids)

    if actors_ids:
        Movie.actors.set(actors_ids)

    return create