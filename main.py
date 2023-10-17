import init_django_orm  # F401


from services import (movie as movie_service,
                      cinema_hall as cinema_service,
                      movie_session)

if __name__ == "__main__":
    print(movie_service.get_movies(genres_ids=[2, 1]))

    print(cinema_service.get_cinema_halls().get(id=1))

    print(movie_session.get_movie_session_by_id(1))
