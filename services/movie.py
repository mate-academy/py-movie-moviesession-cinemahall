from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(genres_ids: int = None, actors_ids: int = None) -> QuerySet[Movie] | None:
    movies = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return movies
    if genres_ids and actors_ids:
        return movies.filter(
            genres__id__in=genres_ids,
            actor__id__in=actors_ids
        )
    elif genres_ids and not actors_ids:
        return movies.filter(genre__id__in=genres_ids)
    elif actors_ids and not genres_ids:
        return movies.filter(actor__id__in=genres_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    movie = Movie.objects.get(id=movie_id)
    return movie


def create_movie(
        movie_title: str,
        movie_description: str = None,
        genres_ids: [int] = None,
        actors_ids: [int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)
    if genres_ids:
        needed_genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(needed_genres)
    if actors_ids:
        needed_actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(needed_actors)

    return movie
