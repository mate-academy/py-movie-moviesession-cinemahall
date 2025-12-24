from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet:

    movie_query = Movie.objects.all()

    if genres_ids is None and actors_ids is None:
        return movie_query

    if actors_ids:
        movie_query = movie_query.filter(actors__id__in=actors_ids)

    if genres_ids:
        movie_query = movie_query.filter(genres__id__in=genres_ids)

    return movie_query


def get_movie_by_id(movie_id: int) -> Movie:
    if movie_id:
        return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
    new_movie.save()
