# Movie, CinemaHall, and MovieSession

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

In `db/models.py` you already have tables you created earlier. Now
you have to create tables:
1. `Movie`, with such fields:
    - char field `title`, the title of the movie with
the maximum length of 255 characters.
    - text field `description`
    - many to many field `actors`, which is related to 
the table `Actor`
    - many to many field `genres`, which is related to 
the table `Genre`

There should be implemented the string representation of the movie:
```python
speed = Movie.objects.create(title="Speed", description="Speed movie")
print(speed)
# Speed
```
2. `CinemaHall`, with such fields:
    - char field `name`, the name of the cinema hall with the maximum
length of 255 characters
    - integer field `rows`, the number of rows of seats in the
hall
    - integer field `seats_in_row`, the number of seats in each row

There should be implemented string representation of the hall and
the `capacity` property that returns total number of seats in the hall:
```python
blue = CinemaHall.objects.create(name="Blue", rows=9, seats_in_row= 13) 

print(blue)
# Blue

print(blue.capacity)
# 117
```
3. `MovieSession`, with such field:
    - date time field `show_time`, the date and the time of the movie session
performance
    - foreign key `cinema_hall`, the hall where the movie session is performed,
references to the table `CinemaHall`
    - foreign key `movie`, the movie to be shown, references 
to the table `Movie`
    
There should be implemented string representation of the movie session,
that shows the movie name, the date, and the time of the movie session:

```python
import datetime

movie_session = MovieSession.objects.create(
    show_time=datetime.datetime(year=2021, month=11, day=29, hour=16, minute=40),
    cinema_hall=blue,
    movie=speed
)

print(movie_session)
# Speed 2021-11-29 16:40:00
```
Use the following command to load prepared data from fixture to test and debug your code:
  
`python manage.py loaddata cinema_db_data.json`.

Also, implement a few services for these tables. A service
represents module with functions with queries for the certain 
table.
Create a package `services` next to the package `db`. Inside 
the package `services` create such service modules:
1. `movie.py`, implements such functions:
   - `get_movies`, takes optional `genres_ids` - a list
of genres ids, optional `actors_ids` - a list of actors ids. 
       - If `genres_ids` and `actors_ids` are not provided,
the method returns all movies
       - If both 
`genres_ids` and `actors_ids` are provided, the 
method returns movies, that have at least one genre from `genres_ids` **and**
one actor from `actors_ids`. 
       - If only `genres_ids` is provided, the method returns the queryset
with movies, that have at least one genre from `genres_ids`
       - If only `actors_ids` is provided, the method returns the queryset
with movies, that have at least one actor from `actors_ids`
   - `get_movie_by_id`, takes `movie_id` - id of the movie,
returns movie with the provided id.
   - `create_movie`, takes `movie_title`, `movie_description`, 
optional `genres_ids` and optional `actors_ids`, `genres_ids`
and `actors_ids` are the list of genres ids and the list of actors
ids respectively, method
creates movie with provided title and description, add him genres if
`genres_ids` is provided, add him actors if `actors_ids` is provided.

**Note**: You can use suffix `__id` to get access to the field `id`
of related table inside `.filter()` method. You also can 
use the suffix `__in`  to check if the value is in list/tuple.

2. `cinema_hall.py`, implements such functions:
   - `get_cinema_halls`, returns all cinema halls
   - `create_cinema_hall`, takes `hall_name`, `hall_rows`, `hall_seats_in_row`,
creates cinema hall with provided parameters
3. `movie_session.py`, implements such functions:
   - `create_movie_session`, takes `movie_show_time` - show time of the movie, 
`movie_id` - id of the movie, `cinema_hall_id` - id of the cinema hall. Creates
movie session with provided parameters
   - `get_movies_sessions`, takes optional string `session_date` in such
form: "year-month-day"
       - if `session_date` is provided - returns all movie sessions for this 
date
       - else returns all movies sessions
   - `get_movie_session_by_id`, takes `movie_session_id` - id of the movie 
session, returns movie session with the provided id
   - `update_movie_session`, takes `session_id`, optional `show_time`,
optional `movie_id`, optional `cinema_hall_id`. Update movie session with
provided `session_id` and set fields if appropriate values are provided
   - `delete_movie_session_by_id`, takes `session_id` - id of session,
deletes movie session with the provided id

**Note**: You can use suffix `__date` to get access to date of the 
`DateTimeField`

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
