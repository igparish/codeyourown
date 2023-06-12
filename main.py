import pickle
from os import path

def save (object, file):
    """Serialize a dictionary to a file."""
    with open(file, "wb") as f:
        pickle.dump(object, f)

def load(file):
    """Load a dictionary from a serialized file.
     Or return None if the file doesn't exist."""
    if path.exists(file):
        with open(file, "rb") as f:
            return pickle.load(f)
    return None

FILE = "state.pkl"
d = load (FILE)
if d is None:
    d = {}

print (d)

key = input ("enter a key to add to the dictionary")
value = input ("enter a value to add to the dictionary")
d[key] = value
save (d, FILE)
