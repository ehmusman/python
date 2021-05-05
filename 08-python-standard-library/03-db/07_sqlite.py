import sqlite3
import json
from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())

# with sqlite3.connect("db.sqlite3") as connection:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         connection.execute(command, tuple(movie.values()))
#     connection.commit()

# Reading from sqlitedb

with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command)
    # for movie in cursor:
    #     print(movie) # each movie is a tuple
    print(cursor)
    movies = cursor.fetchall()
    print(movies)
