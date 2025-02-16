from db.models import Movie
from django.db.models import Q


def get_movies(
    genres_id: list[int] | None = None, actors_id: list[int] | None = None
) -> list[Movie]:
    query = Movie.objects.all()
    if genres_id and actors_id:
        query = query.filter(Q(genres__id__in=genres_id)
                             & Q(actors__id__in=actors_id))
    elif genres_id:
        query = query.filter(genres__id__in=genres_id)

    elif actors_id:
        query = query.filter(actors__id__in=actors_id)

    return query.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
