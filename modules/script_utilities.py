import os

def clear_terminal():
    """Clears Terminal"""
    if os.name=='nt': #Windows
        os.system('cls')

    else:
        os.system('clear')

def terminal_pathfind():
    """ Lets terminal users find and/or create directories
    returns path as a string"""
    selected_directory = False # Remains false while no existing directory has been selected

    while not selected_directory:
        current_dir_contents = ' | '.join(map(str, os.listdir()))
        clear_terminal()
        
        print("Current directory is {} \n\nThe directory contains: \n{}".format(os.getcwd(), current_dir_contents))

        choice = input("\nNote: you can use .. to go up a directory and mkdir to create a directory \nPlease select a directory: ")
        if choice.lower() == "mkdir":
            directory_name = str(input("What would you like to call the directory?: "))
            try:
                os.mkdir(directory_name)
            except expression as identifier:
                print("Invalid selection made \nError: {}".format(identifier))
            
        # If they've selected the right folder
        elif choice.lower() == "here":
            chosen_directory = os.getcwd()
            return chosen_directory

        # If user wants to navigate to a different folder
        elif not choice.lower() == "here":
            try:
                os.chdir(choice)
                selection = validate_menu_options(max = 2, min = 1,
                message="Current Path: {} \nWould you like to use the current path? (1)Yes (2)No :".format(os.getcwd()) )

                if selection == 1:
                    chosen_directory = os.getcwd()
                    return chosen_directory
                    selected_directory = True
                else:
                    continue
            except NotADirectoryError:
                print("Invalid selection made choice is not a directory")


def select_directory(gui=True, use_cwd=False):
    # Terminal/cmd based file path selection for headless systems

    if use_cwd == True:
        return str(os.getcwd())

    if gui == False:
        return terminal_pathfind()


    # GUI based file selector
    if gui == True:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        file_path = str(filedialog.askdirectory(
                title="Specify Config File save Location",
                mustexist=False))
        return file_path

def save_config_to_file(data, file_path):
    """Takes two parameters:
    data: JSON formatted data (Dictionary and/or class instance with vars(<instance>))
    file_path: A string representation of the path to output config.json to
    """
    import json
    with open("{}/config.json".format(file_path), "w") as write_file:
        json.dump(data, write_file)


def validate_menu_options(max=1, min=0, message = "Please select option between {} and {}".format(min, max)):
    """
    Takes three parameters:
    max: The maximum value
    min: The minimum value
    Message: A message to explain what selections are possible
    """
    valid_answer = False
    while valid_answer == False:
        try:
            selection = eval(input(message))
        except:
            print("Invalid input please try again")
        
        # More than max
        if selection > max:
            print("Invalid input the selection made was larger than {}".format(max))
        #Less than min
        elif selection < min:
            print("Invalid input the selection made was smaller than {}".format(min))

        #just Right
        else:
            return selection
            valid_answer = True
            

class terminal_menu:
    def __init__(self, title = "Menu title" ):
        pass