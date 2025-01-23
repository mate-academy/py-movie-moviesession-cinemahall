from db.models import Movie, MoveSession, CinemaHall


def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    except Movie.DoesNotExist:
        raise ValueError("Movie with this ID does not exist.")
    except CinemaHall.DoesNotExist:
        raise ValueError("Cinema Hall with this ID does not exist.")

    movie_session = MoveSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )

    return movie_session