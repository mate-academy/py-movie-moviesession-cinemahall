from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: int = None,
        actors_ids: int = None
) -> Movie:
    movies_queryset = Movie.objects.all()

    if genres_ids is not None:
        movies_queryset = movies_queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        movies_queryset = movies_queryset.filter(actors__id__in=actors_ids)

    return movies_queryset


def get_movie_by_id(movie_id: int) -> Movie:
    movie = Movie.objects.get(id=movie_id)
    return movie


def create_movie(
        movie_title: Movie,
        movie_description: str,
        genres_ids: int = None,
        actors_ids: int = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(Genre.objects.filter(id__in=genres_ids))
    if actors_ids:
        movie.actors.set(Actor.objects.filter(id__in=actors_ids))
    return movie
