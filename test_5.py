#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.state import State

# Instantiate FileStorage
fs = FileStorage()

# Reload the previously saved data
fs.reload()

# Get all states from the storage
all_states = fs.all(State)

print("All States: {}".format(len(all_states.keys())))

for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State instance
new_state = State()
new_state.name = "California"

# Add the new state to the storage
fs.new(new_state)

# Save the changes
fs.save()

print("New State: {}".format(new_state))

# Reload the data again
fs.reload()

# Get all states from the storage
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))

for state_key in all_states.keys():
    print(all_states[state_key])

