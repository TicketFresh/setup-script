"""
Contains all the utilities needed to create and/or configure ticketfresh instances
Available Commands:
    setup; allows you to set up new ticketfresh instances
    config; Allows you to change the configuration of the instance defined in toolbox
"""
import argparse
from modules.configure_instance import configuration_menu

if __name__ == "__main__":
    # Setting up Main Argument Parser
    main_parser = argparse.ArgumentParser(description="Toolbox for setting up and configuring TicketFresh instance")
    main_parser.add_argument("-v",'--version', action='version', version='TicketFesh Toolbox V0.1')

    # Setting up the main subparser
    subparsers = main_parser.add_subparsers(help="Available commands found below, for more info on a command use: python toolbox.py <command> -h")

    """ All the code for creating new ticketfresh instances
    Called via python toolbox.py setup"""
    setup_parser = subparsers.add_parser('setup',
        help='Creates a new ticketfresh instance')
    setup_parser.add_argument('-d', "--default",
        help='Creates instance with all default settings')
    setup_parser.add_argument('-l', "--local",
        help='Skip all dialogues and create a new')
    setup_parser.add_argument('-ng', "--no_gui",
        help="Used in headless OS systems so the tkinter file dialog dosen't appear")


    """ All the code for initializing the configuration parser 
    Called via python toolbox.py config"""
    config_parser = subparsers.add_parser('config', argument_default='-m',
        help='Allows you to configurean existing TicketFresh instance')
    config_parser.add_argument('-d', "--default",
        help='Sets all instance settings back to default settings')
    config_parser.add_argument('-m', "--menu", action='store_true',
        dest="config_menu", help="allows you to access the configuration menu")
    config_parser.add_argument('-ng', "--no_gui",
        help="Used in headless OS systems so the tkinter file dialog dosen't appear")


    """ All the code for initializing the monitoring parser 
    Called via python toolbox.py monitor"""
    config_parser = subparsers.add_parser('monitor', argument_default='-m',
        help='Allows you to configurean existing TicketFresh instance')
    config_parser.add_argument('-m', "--menu", action='store_true',
        dest="monitor_menu", help="allows you to access the monitoring menu")
    config_parser.add_argument('-ng', "--no_gui",
        help="Used in headless OS systems so the tkinter file dialog dosen't appear")

    # Obligatory argument parsing, setting arguments to args for later use
    args = main_parser.parse_args()

    if args.config_menu:
        configuration_menu()