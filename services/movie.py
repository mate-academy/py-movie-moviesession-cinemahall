from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list = None,
               actors_ids: list = None) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        movies = movies.filter(
            genres__id__in=genres_ids,
            actor__id__in=actors_ids
        )
    elif genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    elif actors_ids:
        movies = movies.filter(actor__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.filter(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_id: list = None, actors_id: list = None
                 ) -> QuerySet:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_id:
        movie.genres.add(genres_id=genres_id)
    if actors_id:
        movie.actors.add(actors_id=actors_id)
