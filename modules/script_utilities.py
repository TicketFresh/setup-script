import os

def clear_terminal():
    """Clears Terminal"""
    if os.name=='nt': #Windows
        os.system('cls')

    else:
        os.system('clear')

def get_ip():
    if os.name=='nt': #Windows
        return "ipconfig"

    else:
        return "ifconfig"


def select_directory(gui=True, use_cwd=False):
    # Terminal/cmd based file path selection for headless systems

    if use_cwd == True:
        return str(os.getcwd())

    if gui == False:
        #TODO Figure out how to do a path selection in terminal
        pass

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


def validate_menu_options(max=1, min=0):
    """
    Takes three parameters:
    max: The maximum value
    min: The minimum value
    options: A dictionary with the option numbers as the keys, and the function calls as the values
    text: The text to explain what each option does
    """
    valid_answer = False
    while valid_answer == False:
        try:
            selection = eval(input("What is your selection?: "))
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
            


if __name__ == "__main__":
    validate_menu_options()