from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list[Genre] = None,
        actors_ids: list[Actor] = None ) -> QuerySet:

    movie_query = Movie.objects.all()

    if genres_ids is None and actors_ids is None:
        return movie_query

    if genres_ids:
        movie_query = Movie.objects.filter(genres__id__in=genres_ids)
    if actors_ids:
        movie_query = Movie.objects.filter(actors__id__in=actors_ids)

    return movie_query

def get_movie_by_id(movie_id: int) -> Movie:
    if movie_id:
        return Movie.objects.get(id=movie_id)

def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int]  = None,
                 actors_ids: list[int] = None) -> None:
    new_movie = Movie.objects.create(
        title = movie_title,
        description = movie_description,
        genres_ids = genres_ids,
        actors_ids = actors_ids
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)



