from django.db.models import QuerySet

from db.models import Movie


def get_movies(
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None
) -> QuerySet[Movie]:
    if actors_ids and genres_ids:
        return Movie.objects.filter(
            actors__id__in=actors_ids,
            genres__id__in=genres_ids
        )
    elif genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)
    elif actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)

    return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    actors_ids: list[int] = None,
    genres_ids: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if actors_ids is not None:
        movie.actors.set(actors_ids)
    if genres_ids is not None:
        movie.genres.set(genres_ids)

    return movie
