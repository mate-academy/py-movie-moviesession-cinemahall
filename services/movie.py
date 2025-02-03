from db.models import Movie, Actor, Genre


def get_movies(genres_ids: int = None, actors_ids: int = None) -> None:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if genres_ids and actors_ids:
        return Movie.objects.filter(genres__in=genres_ids,
                                    actors__in=actors_ids)

    if genres_ids:
        return Movie.objects.filter(genres__in=genres_ids)

    if actors_ids:
        return Movie.objects.filter(actors__in=actors_ids)

    return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> None:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 actors_ids: list[int] = None,
                 genres_ids: list[int] = None) -> None:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if actors_ids:
        actor = Actor.objects.get(id__in=actors_ids)
        movie.actors.add(actor)

    if genres_ids:
        genre = Genre.objects.get(id__in=genres_ids)
        movie.genres.add(genre)

    return movie
