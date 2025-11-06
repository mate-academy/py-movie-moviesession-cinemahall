from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None):
    if genres_ids == None and actors_ids == None:
        return Movie.objects.all()

    if genres_ids and actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids, actors__id__in=actors_ids)

    if genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)

    if actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)

def get_movie_by_id(movie_id):
    return Movie.objects.get(id=movie_id)

def create_movie(movie_title, movie_description, genres_ids=None, actors_ids=None):
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids is not None:
        movie.genres.add(*genres_ids)

    if actors_ids is not None:
        movie.actors.add(*actors_ids)

    return movie
