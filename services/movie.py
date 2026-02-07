from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        queryset = queryset.filter(genres__id__in=genres_ids,
                                   actors__id__in=actors_ids)
    elif genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    elif actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie | None:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None) -> Movie:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)

    if genres_ids:
        movie.genres.add(*genres_ids)

    if actors_ids:
        movie.actors.add(*actors_ids)

    return movie
