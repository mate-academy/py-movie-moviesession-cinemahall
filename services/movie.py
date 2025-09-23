from db.models import Genre, Actor, Movie


def get_movies(genres_ids, actors_ids):
    movies = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return movies
    elif genres_ids and actors_ids:
        movies = Movie.objects.filter(genres__id__in=genres_ids, actors__id__in=actors_ids).distinct()
        return movies
    elif genres_ids and not actors_ids:
        movies = Movie.objects.filter(genres__id__in=genres_ids).distinct()
        return movies
    else:
        movies = Movie.objects.filter(actors__id__in=actors_ids).distinct()
        return movies

def get_movie_by_id(movie_id):
    movie = Movie.objects.get(id=movie_id)
    return movie

def create_movie(movie_title, movie_description, genres_ids, actors_ids):
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie