from django.db.models import QuerySet

from db.models import Movie


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> Movie | QuerySet:
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()
    elif genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids).distinct()
    elif actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids).distinct()
    else:
        return Movie.objects.all()


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
    return new_movie
