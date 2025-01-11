from django.db.models import QuerySet

from db.models import Movie

def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet:
    if genres_ids:
        return Movie.objects.filter(genres__in=genres_ids)
    if actors_ids:
        return Movie.objects.filter(actors__in=actors_ids)
    return Movie.objects.all()

def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)

def create_movie(title: str,
                 description: str,
                 genres_ids: list[int],
                 actors_ids: list[int]) -> None:
    movie = Movie.objects.create(title=title,
                         description=description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
