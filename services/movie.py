import datetime
from db.models import Genre, Movie, Actor

def get_movies(genres_ids=None, actor_ids=None):
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genre__id__in=genres_ids)

    if actor_ids:
        queryset = queryset.filter(actor__id__in=actor_ids)

    return queryset.distinct()

def get_movie_by_id(movie_id):
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None


def create_movie(movie_title: str, movie_description: str, genre_ids=None, actor_ids=None):
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genre_ids:
        genres = Genre.objects.filter(id__in=genre_ids)
        movie.genres.add(*genres)

    if actor_ids:
        actors = Actor.objects.filter(id__in=actor_ids)
        movie.actors.add(*actors)

    return movie
