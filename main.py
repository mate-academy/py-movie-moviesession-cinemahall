
import init_django_orm # noqa F401


from services import movie_session as movie_session_service

if __name__ == "__main__":
    # print(movie_service.get_movies(actors_ids=[2], genres_ids=[1]))
    # print(movie_service.get_movie_by_id(2))
    # print(movie_service.create_movie(
    #     movie_title="Terminator",
    #     movie_description="Give me your clothes",
    #     genres_ids=[1],
    #     actors_ids=[2]
    # ))
    # movie_session_service.update_movie_session(
    #     session_id=1,
    #     show_time=datetime.date(year=2023, month=1, day=1),
    #     movie_id=2,
    #     cinema_hall_id=2
    # )
    movie_session_service.delete_movie_session(1)
