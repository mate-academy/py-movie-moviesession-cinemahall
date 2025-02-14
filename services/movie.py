from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet[Movie] | None:
    movies = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return movies

    if genres_ids and actors_ids:
        movies = movies.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()

    elif genres_ids:
        movies = movies.filter(genres__id__in=genres_ids).distinct()

    elif actors_ids:
        movies = movies.filter(actors__id__in=actors_ids).distinct()

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        genre = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genre)
    if actors_ids:
        actor = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actor)
    return movie
