from django.db.models import QuerySet

from db.models import Actor, Genre, Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies.distinct()


def get_movie_by_id(movie_id: int) -> Movie | None:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        genre = Genre.objects.filter(id__in=genres_ids)
        new_movie.genres.set(genre)
    if actors_ids:
        actor = Actor.objects.filter(id__in=actors_ids)
        new_movie.actors.set(actor)

    return new_movie
