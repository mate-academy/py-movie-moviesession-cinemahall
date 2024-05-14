import init_django_orm  # noqa: F401

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> object:
    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> object:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return f"Movie with id {movie_id} does not exist"


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[Genre] = None,
        actors_ids: list[Actor] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        try:
            genres = Genre.objects.filter(id__in=genres_ids)
            movie.genres.add(*genres)
        except Genre.DoesNotExist:
            print(f"Genre with id {genres_ids} does not exist")
    if actors_ids:
        try:
            actors = Actor.objects.filter(id__in=actors_ids)
            movie.actors.add(*actors)
        except Actor.DoesNotExist:
            print(f"Actor with id {actors_ids} does not exist")
    movie.save()
