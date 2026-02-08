from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    movies_to_return = Movie.objects.all()

    if genres_ids:
        movies_to_return = movies_to_return.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies_to_return = movies_to_return.filter(actors__id__in=actors_ids)

    return movies_to_return


def get_movie_by_id(movie_id: int) -> Movie | None:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        print(f"Movie with id {movie_id} does not exist")


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
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)
