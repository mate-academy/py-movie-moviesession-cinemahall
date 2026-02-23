from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None) -> list[Movie]:

    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if genres_ids and not actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)
    if actors_ids and not genres_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)
    else:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None) -> Movie:

    movie = Movie(title=movie_title, description=movie_description)
    movie.save()

    # for genres_id in genres_ids:
    #     movie.genres.add(genres_id)
    # for actor_id in actors_ids:
    #     movie.actors.add(actor_id)

    if genres_ids:
        movie.genres.add(*genres_ids)

    if actors_ids:
        movie.actors.add(*actors_ids)

    return movie
