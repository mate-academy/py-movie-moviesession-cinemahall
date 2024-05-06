from django.db.models import Q
from db.models import Movie

def get_movies(genres_ids=None, actors_ids=None):

    query = Q()
    if genres_ids:
        query &= Q(genres__id__in=genres_ids)
    if actors_ids:
        query &= Q(actors__id__in=actors_ids)

    return Movie.objects.filter(query).distinct()

def get_movie_by_id(movie_id):

    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None

def create_movie(movie_title, movie_description, genres_ids=None, actors_ids=None):

    movie = Movie(title=movie_title, description=movie_description)
    movie.save()
    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)

    movie.save()
    return movie
