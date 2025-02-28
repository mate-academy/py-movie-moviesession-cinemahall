from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list | None,
               actors_ids: list | None) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        return queryset.filter(genre__in=genres_ids,
                               actor__in=actors_ids)
    if genres_ids:
        queryset = queryset.filter(genre__id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actor__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list | None,
                 actors_ids: list | None) -> Movie:
    movie = Movie(title=movie_title,
                  description=movie_description)
    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)
    return movie

