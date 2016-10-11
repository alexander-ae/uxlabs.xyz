import json
from os.path import join


def get_env(base_dir):
    print base_dir
    print "------------"
    with open(join(base_dir, 'settings/settings.json')) as f:
        env = json.load(f)
        return env
    return {}
