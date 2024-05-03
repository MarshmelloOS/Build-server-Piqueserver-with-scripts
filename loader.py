import os, sys
from piqueserver.config import config

sys.path.append(os.path.join(config.config_dir, 'scripts'))


def apply_script(protocol, connection, config):
    return protocol, connection
