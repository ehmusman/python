import json
from pathlib import Path
movies = [
    {"id": 1, "title": "Terminator", "year": 1998},
    {"id": 2, "title": "Harry potter", "year": 1999},
    {"id": 3, "title": "God father", "year": 2012},
    {"id": 4, "title": "Inspection", "year": 2021},
    {"id": 5, "title": "Inception", "year": 2024},
]


data = json.dumps(movies)
Path("movies.json").write_text(data)
print(data)

# Reading
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0]["title"])