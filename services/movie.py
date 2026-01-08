from db.models import Actor, Genre, Movie


def get_movies(genres_ids=None, actors_ids=None):
    query = Movie.objects.all()

    if genres_ids:
        query = query.filter(genres__id__in=genres_ids)
    if actors_ids:
        query = query.filter(actors__id__in=actors_ids)

    return query.distinct()  # Уникаємо дублікатів


def get_movie_by_id(movie_id):
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title, movie_description, genres_ids=None, actors_ids=None):
    movie = Movie.objects.create(title=movie_title, description=movie_description)

    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)

    return movie
