from db.models import Movie, Genre, Actor


def get_movies(genres_ids=None, actors_ids=None) -> Movie:
    movies_qs = Movie.objects.all()

    if genres_ids:
        movies_qs = movies_qs.filter(genres_id__in=genres_ids).distinct()

    if actors_ids:
        movies_qs = movies_qs.filter(actor_id__in=actors_ids).distinct()
    return movies_qs.first()


def get_movie_by_id(movie_id) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title,
        movie_description,
        genres_ids=None,
        actors_ids=None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        genre = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(genre)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(actors)

    return movie
