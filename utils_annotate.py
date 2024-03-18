import json

def load_json(file):
    with open(file, "r") as f:
        data = json.loads(f.read())
    return data