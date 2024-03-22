from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def get_movies(genres_ids: list[Genre] = None,
               actors_ids: list[Actor] = None) -> QuerySet[Movie]:
    query = Movie.objects.all()

    if actors_ids:
        query = query.filter(actors__in=actors_ids)

    if genres_ids:
        query = query.filter(genres__in=genres_ids)

    return query


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[Genre] = None,
                 actors_ids: list[Actor] = None) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
