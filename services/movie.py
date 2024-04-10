from db.models import Genre, Actor, Movie

from django.db.models import QuerySet


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        for genre_id in genres_ids:
            genre = Genre.objects.get(id=genre_id)
            movie.genres.add(genre)
    if actors_ids:
        for actor_id in actors_ids:
            actor = Actor.objects.get(id=actor_id)
            movie.actors.add(actor)
