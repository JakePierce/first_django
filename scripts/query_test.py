#!/usr/bin/env python

import csv
import sys
import os


sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import State, StateCapital, City

#print State.objects.all()
#print State.objects.filter(name__startswith="N")
# state = State.objects.get(pk=153)
# print clown_shoes.abbrev
# states = State.objects.all().order_by('-pop')
# print states

#states = State.objects.all().exclude(name__contains='Ala')
# states = State.objects.all().exclude(name__istartswith='N')

# for state in states:
#     print state.name

#states = State.objects.all().values('name', 'pop')

# for state in states:
#     print state   
# print os.path.abspath(__file__)

# dir_name = os.path.dirname(os.path.abspath(__file__))
# file_name = "states.csv"

# # print "%s/%s" % (dir_name, file_name)

# # print "{0}/{1}".format(dir_name, file_name)

# states_csv = os.path.join(dir_name, file_name)

# csv_file = open(states_csv, 'r')

# reader = csv.DictReader(csv_file)

# for row in reader:
#     new_state, created = State.objects.get_or_create(name=row['state'])
#     new_state.abbrev = row['abbrev']
#     new_state.capital = row['capital']
#     new_state.lat = row['latitude']
#     new_state.lon = row['longitude']
#     new_state.pop = row['population']
#     new_state.save()

#DAY 3 CONTINUED

# states = State.objects.all().values_list('name', 'abbrev', 'pk')

# for state in states:
#     print "State Name: %s, State Abbreviation: %s" % (state[0], state[1])

#states = State.objects.all().values_list('name', 'abbrev', 'pop')

# for name, abbrev, pop in states:
#     print "Name:{2}, Abbrev:{0}, Pop:{1}".format(name, abbrev, pop)

# states = State.objects.all().exclude(name__istartswith='N').filter(pop__gte='500000').order_by('-pop').values_list('name', 'pop')

# print states

# for state in states:
#     #print "%s %s" % (state.name, state.pop)
#     #for dictionaries
#     #print "%s %s" % state['name'], state['pop']
#     #for a list of list using values_list('name', 'pop')
#     print "%s %s" % state[0], state[1]

# states_list = ['Texas', 'California', 'Nevada', 'Alaska']

# states = State.objects.filter(name__in=states_list)

# # print states

# state = State.objects.get(name='Alabama')

# print state.name
# print state.abbrev
# print state.statecapital_set.all()

# state = State.objects.get(pk=56)
# state2 = State.objects.get(pk=34)
# state3 = State.objects.get(pk=33)
# state4 = State.objects.get(pk=32)

# cap = StateCapital.objects.get(pk=1)
# cap = StateCapital.objects.get(pk=2)
# cap = StateCapital.objects.get(pk=3)



# print cap.name
# print state.name

# state.statecapital_set.remove(cap)
# cap.state.add(state)
# cap.state.add(state2)
# cap.state.add(state3)
# cap.state.add(state4)

# state.statecapital_set.add(cap)
# state.statecapital_set.add(cap2)
# state.statecapital_set.add(cap3)
# cap.state.add(state)

# #print state.statecapital_set.all()
# print "---------"
# print state.statecapital_set.all()

# states = State.objects.all()

# for state in states:
#     print "State:%s, Capital:%s" % (state.name, state.statecapital.name)

cities = City.objects.all()[:25]

for city in cities:
    print city
