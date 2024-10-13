import json
import os
from django.core.management.base import BaseCommand
from core.models import Movie, Still, Person, Country, Genre    

# directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# path to master.json
json_file_path = os.path.join(current_dir, 'master.json')

seed_data = None

class Command(BaseCommand):
    help = 'Seed the database with movie data'

    def handle(self, *args, **kwargs):
        # read the json file
        with open(json_file_path, 'r') as file:
            seed_data = json.load(file)

        for movie_data in seed_data:
            movie = Movie.objects.create(
                 imdb_id=movie_data['imdb_id'],
                title=movie_data['title'],
                date_released=movie_data['date_released'],
                genres=movie_data['genre'],
                rating=movie_data['rating'],
                directors=movie_data['director'],
                cinematographers=movie_data['cinematographer'],
                countries=movie_data['country'],
                imdb_rating=movie_data['imdb_rating'],
            )
            

