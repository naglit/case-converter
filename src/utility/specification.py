import os, json

def read_spec(specarg=None):
    """ read a config """

    spec = "spec.json" if specarg == None else specarg
    spec_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", spec)
    with open(spec_path, 'r',encoding="utf-8") as f:
        config = json.load(f)
        return config
