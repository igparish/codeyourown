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


