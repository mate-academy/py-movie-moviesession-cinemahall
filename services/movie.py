from db.models import Movie
from django.db.models import Q


def get_movies(
    genres_ids: list[int] | None = None, actors_ids: list[int] | None = None
) -> list[Movie]:
    query = Movie.objects.all()
    if genres_ids and actors_ids:
        query = query.filter(Q(genres__id__in=genres_ids)
                             & Q(actors__id__in=actors_ids))
    elif genres_ids:
        query = query.filter(genres__id__in=genres_ids)

    elif actors_ids:
        query = query.filter(actors__id__in=actors_ids)

    return query.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_idss: list[int] | None = None,
    actors_idss: list[int] | None = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_idss:
        movie.genres.set(genres_idss)
    if actors_idss:
        movie.actors.set(actors_idss)

    return movie
