from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        actors_ids: list[int] = None,
        genres_ids: list[int] = None
) -> QuerySet[Movie]:
    query_set = Movie.objects.all()
    if actors_ids and genres_ids:
        query_set = query_set.filter(
            actors__id__in=actors_ids,
            genres__id__in=genres_ids
        )
    if actors_ids:
        query_set = query_set.filter(actors__id__in=actors_ids)
    if genres_ids:
        query_set = query_set.filter(genres__id__in=genres_ids)

    return query_set


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: list[int] = None,
        genres_ids: list[int] = None,
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if actors_ids:
        new_movie.actors.set(actors_ids)
    if genres_ids:
        new_movie.genres.set(genres_ids)
    return new_movie
