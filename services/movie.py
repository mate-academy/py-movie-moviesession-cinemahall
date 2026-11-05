from django.db.models import QuerySet
from db.models import Movie


def get_movies(genres_ids: list[int] | None = None, actors_ids: list[int] | None = None) -> QuerySet | Movie:

    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        queryset = queryset.filter(genre_id__in=genres_ids, actor_id__in=actors_ids)
    if genres_ids:
        queryset = queryset.filter(genre_id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actor_id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie | None:
    return Movie.objects.filter(id=movie_id).first()

def create_movie(movie_title: Movie | None, movie_description: Movie | None, /, genres_ids: list[int] | None = None, actors_ids: list[int] | None = None) -> Movie:
    return Movie.objects.create(movie_title=movie_title, movie_description=movie_description, genres=genres_ids, actors=actors_ids)