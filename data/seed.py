import json
import os
from django.core.management.base import BaseCommand
from core.models import Movie, Still, Person, Country, Genre    

# directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# path to master.json
json_file_path = os.path.join(current_dir, 'master.json')

seed_data = None

# Read and print the JSON file
try:
    with open(json_file_path, 'r') as file:
        seed_data = json.load(file)
    print(json.dumps(seed_data, indent=2))
except FileNotFoundError:
    print(f"Error: The file {json_file_path} was not found.")
except json.JSONDecodeError:
    print(f"Error: The file {json_file_path} is not valid JSON.")


