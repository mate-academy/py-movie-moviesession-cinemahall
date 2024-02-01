from db.models import Movie
from django.db.models import QuerySet

def get_movies(genres_ids: list[int] = None, actors_ids: list[int] = None) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres_ids) 

    if actors_ids:
        queryset = queryset.filter(actors_ids)
    
    return queryset


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> Movie:
    
    return  Movie.objects.create(
        title=movie_title,
        description=movie_description,
        genres = genres_ids,
        actors = actors_ids
        )