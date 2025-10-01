from django.db.models import QuerySet
from db.models import Actor, Genre, Movie


def get_movies(genre_ids: list[int] = None,
               actor_ids: list[int] = None) -> QuerySet[Movie]:
    movies = Movie.objects.all()
    if genre_ids:
        movies = movies.filter(genres__in=genre_ids)
    if actor_ids:
        movies = movies.filter(actors__in=actor_ids)
    return movies.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genre_ids: list[int] = None,
                 actor_ids: list[int] = None, ) -> Movie:
    movie = Movie.objects.create(title=movie_title, description=movie_description)
    if genre_ids:
        movie.genres.set(Genre.objects.filter(id__in=genre_ids))
    if actor_ids:
        movie.actors.set(Actor.objects.filter(id__in=actor_ids))

    return movie
