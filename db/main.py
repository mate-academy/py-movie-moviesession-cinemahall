import init_django_orm

from services import cinema_hall, movie, movie_session

if __name__ == '__main__':

    print(cinema_hall.get_cinema_halls())

    print(movie.create_movie(title="Speed", description="Speed movie"))

    print(movie_session.create_movie_session(name="Blue", rows=9, seats_in_row= 13))




