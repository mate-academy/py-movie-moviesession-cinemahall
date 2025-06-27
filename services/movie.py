from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list[int] | None,
               actors_ids: list[int] | None = None) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset.distinct()

def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)

def create_movie(movie_title: str, movie_description: str,
                 movie_genres: list[int] | None = None,
                 movie_actors: list[int] | None = None) -> Movie:
    movie = Movie.objects.create(title=movie_title, description=movie_description)
    if movie_genres:
        movie.genres.add(*movie_genres)
    if movie_actors:
        movie.actors.add(*movie_actors)
    return movie
