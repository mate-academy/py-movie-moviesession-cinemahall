from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None,
) -> QuerySet:
    query = Movie.objects.all()
    if genres_ids:
        query.filter(
            genres__id__in=genres_ids
        )
    if actors_ids:
        query.filter(
            actors__id__in=actors_ids
        )

    return query


def get_movie_by_id(id_: int) -> Movie:
    return Movie.objects.get(id_)


def create_movie(
    movie_title: str,
    movie_description: str,
    /,
    genres_ids: list[int] | None = None,
    actors_ids: list[int] | None = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        for genre_id in genres_ids:
            genre = Genre.objects.get(genre_id)
            movie.genres.add(genre)

    if actors_ids:
        for actor_id in actors_ids:
            actor = Actor.objects.get(actor_id)
            movie.actors.add(actor)

    return movie
