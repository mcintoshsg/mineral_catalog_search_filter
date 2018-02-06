''' simple load function to create data in our minerals daatbase'''

import json
import os
import sys
from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.join(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "minerals_site.settings")

sys.path.append(project_path)

application = get_wsgi_application()

from minerals.models import Mineral

def read_data(data_dir):
    ''' inital load of data into the Mineral model '''
    minerals = Mineral.objects.all()
    if not minerals:
        try:
            with open(data_dir + '/minerals.json') as data_file:
                mineral_data = json.load(data_file)
        except FileNotFoundError:
            print('json file does not exits')
        else:
            load_data(mineral_data)
    else:
        print("Database already has stored data")

def load_data(mineral_data):
    ''' loop through the daat and add to database '''
    for mineral in mineral_data:
        try:
            Mineral(
                name=mineral.get('name', ''),
                img_filename=mineral.get('name', '') + '.jpg',
                img_caption=mineral.get('image caption', ''),
                category=mineral.get('category', ''),
                formula=mineral.get('formula', ''),
                strunz_classification=mineral.get('strunz classification', ''),
                crystal_system=mineral.get('crystal system', ''),
                unit_cell=mineral.get('unit cell', ''),
                color=mineral.get('color', ''),
                crystal_symmetry=mineral.get('crystal symmetry', ''),
                cleavage=mineral.get('cleavage', 'Empty'),
                mohs_hardness=mineral.get('mohs scale hardness', ''),
                luster=mineral.get('luster', ''),
                streak=mineral.get('streak', ''),
                diaphaneity=mineral.get('diaphaneity', ''),
                optical_properties=mineral.get('optical properties', ''),
                refractive_index=mineral.get('refractive index', ''),
                crystal_habit=mineral.get('crystal habit', ''),
                specific_gravity=mineral.get('specific gravity', ''),
                group=mineral.get('group', ''),
                ).save()
        except ValueError:
            print('There was a databae error... Exiting!')
            sys.exit()
    print('Mineral data has been successfully added!')

if __name__ == '__main__':
    print(os.path.join(BASE_DIR, 'data'))
    read_data(os.path.join(BASE_DIR, 'data'))
            