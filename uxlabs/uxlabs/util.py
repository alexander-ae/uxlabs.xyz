import json
from os.path import join


def get_env(base_dir):
    with open(join(base_dir, 'uxlabs/settings/settings.json')) as f:
        env = json.load(f)
        return env
