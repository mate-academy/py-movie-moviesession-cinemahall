from django.db.models import QuerySet

from db.models import Genre, Actor, Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)

    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)

    return movies.distinct()


def get_movie_by_id(movie_id: int) -> Movie | None:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        print(f"Movie by id: {movie_id} does not exist!")
        return None


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: list[int] = None,
        genres_ids: list[int] = None
) -> Movie:
    movie, create = Movie.objects.get_or_create(
        title=movie_title,
        defaults={
            "description": movie_description
        }
    )
    if actors_ids:
        valid_actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(valid_actors)

    if genres_ids:
        valid_genre = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(valid_genre)

    if not create:
        print(f"The movie with name: {movie_title} already exist!")

    return movie
