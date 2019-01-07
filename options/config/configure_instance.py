"""
This file contains all the functions and menu used 
when calling the toolbox via the configure command
"""
from kusu.utilities import \
    save_to_json, select_directory

import json
import os

from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.menu_component import Dimension



class ticketfresh_configuration:
    def __init__(self, organization_name, db, domain_name):
        self.organization_name = organization_name
        self.db = db
        self.domain_name = domain_name

DEFAULT_CONFIG = ticketfresh_configuration("Example Organization", "MongoDB", "example.com")


class configuration_menu_state:
    def __init__(self, config_path=str(os.getcwd())):
        self.config_path = config_path
    def change_path_test(self, path):
        self.config_path = path

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
    print(os.getcwd())
    menu_state = json.load("menu_state.json")
    print(menu_state)
    CONFIG_PATH = menu_state["config_path"]

    # Prettying up the window with some formatting
    menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_OUTER_LIGHT_INNER_BORDER)\
        .set_prompt("Selection: ") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_left_margin(4) \
        .set_right_margin(4) \
        .show_header_bottom_border(True)

    # Creating the initial Menu
    menu = ConsoleMenu("Configure TicketFresh", epilogue_text="Select an option from above list",
        prologue_text="The Currently Defined Config path is {}".format(CONFIG_PATH),
        formatter=menu_format)

    # Option lets you export a default conf to the config path
    exp_default_conf = FunctionItem(
        "Export Default config to main directory", save_to_json,
        [vars(DEFAULT_CONFIG), CONFIG_PATH])

    # Option lets you change the config path
    chng_conf_path = FunctionItem(
        "Change current configuration path", select_directory,
        kwargs={"gui":False}
        )

    chng_path_test = FunctionItem(
        "Change current configuration path", menu_state.change_path_test,
        args="Hello World"
        )

    # Adding items to the menu
    menu.append_item(exp_default_conf)
    menu.append_item(chng_conf_path)
    menu.append_item(chng_path_test)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()