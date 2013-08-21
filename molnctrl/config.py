import os
import ConfigParser

class Config(object):
    """ Provides config file support
    """
    def __init__(self):
        config_file = os.getenv('MOLN_CONF', '.moln.conf')
        for loc in os.curdir, os.path.expanduser("~"), os.environ.get('PWD'), '':
            if os.path.exists(os.path.join(loc,config_file)):
                try:
                    config = ConfigParser.ConfigParser()
                    config.read(os.path.join(loc,config_file))
                    return config
                except IOError:
                    config = None
                    return config

