import init_django_orm  # noqa: F401
import json
from datetime import datetime
from db.models import Movie, Genre, Actor, CinemaHall, MovieSession


def main() -> None:
    with open("cinema_db_data.json") as file:
        data = json.load(file)
    for row in data:
        if row["model"] == "db.cinemahall":
            CinemaHall.objects.create(id=row["pk"],
                                      name=row["fields"]["name"],
                                      rows=row["fields"]["rows"],
                                      seats_in_row=row["fields"]
                                      ["seats_in_row"])
        if row["model"] == "db.genre":
            Genre.objects.create(id=row["pk"],
                                 name=row["fields"]["name"])
        if row["model"] == "db.actor":
            Actor.objects.create(id=row["pk"],
                                 first_name=row["fields"]["first_name"],
                                 last_name=row["fields"]["last_name"])
        if row["model"] == "db.movie":
            movie_new = Movie.objects.create(id=row["pk"],
                                             title=row["fields"]["title"],
                                             description=row["fields"]
                                             .get("description"))
            for actor_id in row["fields"]["actors"]:
                actor = Actor.objects.get(id=actor_id)
                movie_new.actors.add(actor)
            for genres_id in row["fields"]["genres"]:
                genre = Genre.objects.get(id=genres_id)
                movie_new.genres.add(genre)
            movie_new.save()
        if row["model"] == "db.moviesession":
            cinema_hall = CinemaHall.objects.get(
                id=row["fields"]["cinema_hall"])
            movie_new = Movie.objects.get(id=row["fields"]["movie"])
            date_string = row["fields"]["show_time"]
            dt_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
            MovieSession.objects.create(id=row["pk"],
                                        show_time=dt_object,
                                        movie=movie_new,
                                        cinema_hall=cinema_hall)


if __name__ == "__main__":
    main()
