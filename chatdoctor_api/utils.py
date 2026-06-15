import json
import datetime

def get_timestamp():

    return str(
        datetime.datetime.now()
    )


def save_json(data, path):

    with open(path, "w") as f:

        json.dump(data, f, indent=4)


def load_json(path):

    with open(path, "r") as f:

        return json.load(f)
