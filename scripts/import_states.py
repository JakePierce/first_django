#!/usr/bin/env python

import csv
import sys
import os


sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()

from main.models import State, StateCapital, City
print os.path.abspath(__file__)

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "zip_codes_states.csv"

# print "%s/%s" % (dir_name, file_name)

# print "{0}/{1}".format(dir_name, file_name)

states_csv = os.path.join(dir_name, file_name)

csv_file = open(states_csv, 'r')

reader = csv.DictReader(csv_file)

# for row in reader:
#     new_state, created = State.objects.get_or_create(name=row['state'])
#     new_state.abbrev = row['abbrev']
#     new_state.save()

#     new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])
#     new_capital.lat = row['latitude']
#     new_capital.lon = row['longitude']
#     new_capital.pop = row['population']

#     new_capital.state = new_state
#     new_capital.save()

for row in reader:
    new_area, created = City.objects.get_or_create(name=row['city'])
    new_area.zip_code = row['zip_code']
    new_area.lat = row['latitude']
    new_area.lon = row['longitude']
    new_area.city = row['city']
    new_area.abbrev = row['state']
    new_area.county = row['county']


    # state = State.objects.get()

    try:
        state_obj = State.objects.get(abbrev=row['state'])
        new_area.state = state_obj
    except:
        print row['state']

    try:
        new_area.save()
    except Exception, e:
        print e


