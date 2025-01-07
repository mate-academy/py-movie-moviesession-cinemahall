from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_id: list = None,
        actors_id: list = None,
) -> QuerySet:
    if not genres_id and not actors_id:
        return Movie.objects.all()

    movies = Movie.objects.all()

    if genres_id:
        movies = movies.filter(genre__in=genres_id)
    if actors_id:
        movies = movies.filter(actor__in=actors_id)

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_id: list = None,
        actors_id: list = None,

) -> Movie:
    if not genres_id and not actors_id:
        return Movie.objects.create(
            title=movie_title,
            description=movie_description
        )

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_id:
        movie.genres.add(*genres_id)
    if actors_id:
        movie.actors.add(*actors_id)

    return movie
