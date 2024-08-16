from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> QuerySet:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    if genres_ids is not None and actors_ids is not None:
        return Movie.objects.filter(
            genres__pk__in=genres_ids,
            actors__pk__in=actors_ids
        )
    if genres_ids is not None and actors_ids is None:
        return Movie.objects.filter(
            genres__pk__in=genres_ids
        )
    if actors_ids is not None and genres_ids is None:
        return Movie.objects.filter(
            actors__pk__in=actors_ids
        )


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None,
                 ) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids is not None:
        new_movie.genres.set(genres_ids)

    if actors_ids is not None:
        new_movie.actors.set(actors_ids)

    new_movie.save()
