"""
This file contains all the functions and menu used 
when calling the toolbox via the configure command
"""
from modules.script_utilities import \
    save_config_to_file, select_directory

import json
import os

from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.menu_component import Dimension



class configuration:
    def __init__(self, organization_name, db, domain_name):
        self.organization_name = organization_name
        self.db = db
        self.domain_name = domain_name

DEFAULT_CONFIG = configuration("Example Organization", "MongoDB", "example.com")

def import_config():
    from pathlib import Path
    import time

    config_file = Path("config.json")

    # If a config file exists in the defualt location
    if config_file.is_file():
        pass

    # Create a config file
    elif not config_file.is_file():
        print("Please Specify a location to save the configuration file to")
        time.sleep(1.5)
        dir = select_directory()
        # TODO Save JSON object

def configuration_menu():
    """ 
    The main configuration menu
    """

    # TODO: Recreate without the console menu module
    CONFIG_PATH = str(os.getcwd())