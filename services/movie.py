from django.db.models import QuerySet
from db.models import Genre, Actor, Movie


def get_movies(genres_ids: list[Genre] = None, /,
               actors_ids: list[Actor] = None
               ) -> QuerySet:
    query = Movie.objects.all()
    if genres_ids and actors_ids:
        query = Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )
    elif genres_ids:
        query = Movie.objects.filter(genres__id__in=genres_ids)
    elif actors_ids:
        query = Movie.objects.filter(actors__id__in=actors_ids)
    return query


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str, /,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        genre = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genre)

    if actors_ids:
        actor = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actor)
    return movie
