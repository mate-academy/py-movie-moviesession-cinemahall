from django.db.models import QuerySet

from db.models import Movie


def get_movie(genres_ids: list[int], actors_ids: list[int]) -> QuerySet:
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres_id__in=genres_ids,
            actors_id__in=actors_ids
        )
    if genres_ids:
        return Movie.objects.filter(genres_id__in=genres_ids)
    if actors_ids:
        return Movie.objects.filter(actors_id__in=actors_ids)

    return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        /,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
):
    movie = Movie(
        movie_title=movie_title,
        movie_description=movie_description
    )
    if genres_ids:
        movie.genres.set(*genres_ids)
    if actors_ids:
        movie.actors.set(*actors_ids)
