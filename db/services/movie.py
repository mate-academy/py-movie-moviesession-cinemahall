from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet[Movie] | None:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids).filter(actors__id__in=actors_ids)
    if genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)
    if actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int)-> QuerySet[Movie] | None:
    return Movie.objects.filter(id=movie_id)


def create_movie(movie_title: str, movie_description: str, genres_ids: list = None, actors_ids: list = None):
    movie = Movie.objects.create(title=movie_title, description=movie_description)

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        for genre in genres:
            movie.genres.add(genre)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        for actor in actors:
            movie.actors.add(actor)

    return movie