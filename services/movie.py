from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet | Movie:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        return movies.filter(
            genres__in=genres_ids,
            actors__in=actors_ids
        )
    if genres_ids:
        return movies.filter(genres__in=genres_ids)
    if actors_ids:
        return movies.filter(actors__in=actors_ids)
    return movies


def get_movie_by_id(id_: int) -> Movie:
    return Movie.objects.get(id=id_)


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: list[int] = None,
        genres_ids: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if actors_ids and genres_ids:
        movie.actors.set(actors_ids)
        movie.genres.set(genres_ids)
        return movie
    if actors_ids:
        movie.actors.set(actors_ids)
        return movie
    if genres_ids:
        movie.genres.set(genres_ids)
        return movie
    return movie
