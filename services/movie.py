from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list[int], actors_ids: list[int]) -> Movie:
    if not genres_ids or not actors_ids:
        return Movie.objects.all()
    if genres_ids or actors_ids:
        return Movie.objects.filter(id__in=genres_ids).filter(id__in=actors_ids)
    if genres_ids:
        return Movie.objects.filter(id__in=genres_ids)
    if actors_ids:
        return Movie.objects.filter(id__in=actors_ids)


def get_movie_by_id(movie_id:int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: int=None,
                 actors_ids: int=None,
                 ) -> Movie:
    movie=Movie.objects.create(title=movie_title, description=movie_description)
    if genres_ids:
        genres=Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids:
        actors=Actor.objects.filter(id__in=actors_ids)
        movie.genres.set(actors)
    return movie
