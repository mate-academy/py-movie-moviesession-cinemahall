from django.db.models import QuerySet
from db.models import Movie


def get_movies(genres_ids: list[int] | None = None,
               actors_ids: list[int] | None = None) -> QuerySet[Movie]:
    movies = Movie.objects.all()
    if genres_ids and actors_ids:
        movies = (movies.filter(genres__id__in=genres_ids).
                  filter(actors__id__in=actors_ids))
    elif genres_ids:
        movies = Movie.objects.filter(genres__id__in=genres_ids)
    elif actors_ids:
        movies = Movie.objects.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Movie | None:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] | None = None,
                 actors_ids: list[int] | None = None) -> Movie:
    movie = Movie(
        title=movie_title,
        description=movie_description)
    movie.save()
    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)
    movie.save()
    return movie
