from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet[Movie]:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if actors_ids and not genres_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)

    if genres_ids and not actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)

    return Movie.objects.filter(
        actors__id__in=actors_ids,
        genres__id__in=genres_ids
    )


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    created_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        created_movie.genres.set(genres_ids)

    if actors_ids:
        created_movie.actors.set(actors_ids)

    return created_movie
