from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet[Movie]:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            actors__in=actors_ids, genres__in=genres_ids
        ).distinct()
    if genres_ids is not None and actors_ids is None:
        return Movie.objects.filter(genres__in=genres_ids).distinct()
    if actors_ids is not None and genres_ids is None:
        return Movie.objects.filter(actors__in=actors_ids).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> Movie:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
