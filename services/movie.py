from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids is None and actors_ids is None:
        return movies

    if genres_ids is not None and actors_ids is not None:
        return movies.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids
        )

    if genres_ids is not None:
        return movies.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        return movies.filter(actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)

    movie.save()
    return movie
