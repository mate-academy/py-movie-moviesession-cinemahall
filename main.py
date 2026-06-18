import init_django_orm
from services.movie_session import get_movies_sessions, create_movie_session
from datetime import datetime

sessions = get_movies_sessions()
print("Поточні сесії:", sessions)
