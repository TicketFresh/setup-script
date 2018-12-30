"""
This file contains all the functions and menu used 
when calling the toolbox via the configure command
"""
from modules.script_utilities import \
    save_config_to_file, select_directory, get_ip

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

def configuration_menu(CONFIG_PATH = "{}/config.json".format(str(os.getcwd()))):
    """ 
    The main configuration menu
    """
    
    # Prettying up the window with some formatting
    menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_OUTER_LIGHT_INNER_BORDER)\
        .set_prompt("SELECT>") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_left_margin(4) \
        .set_right_margin(4) \
        .show_header_bottom_border(True)

    # Creating the initial Menu
    menu = ConsoleMenu("Configure TicketFresh",
        epilogue_text="Select an Option from the choices above",
        prologue_text="The Currently Defined Config path is {}".format(CONFIG_PATH),
        formatter=menu_format)

    # Option lets you export a default conf to the config path
    exp_default_conf = FunctionItem(
        "Export Default config to main directory", save_config_to_file,
        [vars(DEFAULT_CONFIG), CONFIG_PATH])

    # Option lets you change the config path
    chng_conf_path = FunctionItem(
        "Change current configuration path", select_directory,
        kwargs={"gui":False}
        )

    # A CommandItem runs a console command
    create_configuration_directory = CommandItem("Creae a directory called configurations",  "mkdir configurations")

    # Adding items to the menu
    menu.append_item(exp_default_conf)
    menu.append_item(chng_conf_path)
    menu.append_item(create_configuration_directory)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()