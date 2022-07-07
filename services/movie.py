from db.models import Movie

data = Movie.objects.all()


def get_movies(genres_ids=None, actors_ids=None):
    if genres_ids and actors_ids:
        return data.filter(genres__id__in=genres_ids).\
            filter(actors__id__in=actors_ids)
    if genres_ids:
        return data.filter(genres__id__in=genres_ids)
    if actors_ids:
        return data.filter(actors__id__in=actors_ids)
    return data


def get_movie_by_id(movie_id):
    return data.get(id=movie_id)


def create_movie(movie_title, movie_description,
                 genres_ids=None, actors_ids=None):
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
