from django.db.models import QuerySet
from db.models import Movie, Genre, Actor


def get_movies(
    genres_ids: list[int] = None,
    actors_ids: list[int] = None
) -> QuerySet[Movie]:

    if not genres_ids and not actors_ids:
        movies = Movie.objects.all()
        return movies

    if genres_ids and actors_ids:
        movies = Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )
        return movies

    if genres_ids and not actors_ids:
        movies = Movie.objects.filter(genres__id__in=genres_ids)
        return movies

    if actors_ids and not genres_ids:
        movies = Movie.objects.filter(actors__id__in=actors_ids)
        return movies


def get_movie_by_id(movie_id: int) -> Movie | str:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return "Movie not found"


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:

    created_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        genre = Genre.objects.filter(id__in=genres_ids)
        created_movie.genres.set(genre)

    if actors_ids:
        actor = Actor.objects.filter(id__in=actors_ids)
        created_movie.actors.set(actor)

    return created_movie
