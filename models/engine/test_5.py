#!/usr/bin/python3

from file_storage import FileStorage
from models.state import State

fs = FileStorage

all_states = fs.all(State)

print("All States: {}".format(len(all_states.keys())))

for state_key in all_states.keys():
    print(all_states[state_key])
