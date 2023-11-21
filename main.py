import os
import shutil
import re

def main():
    regex_pattern = "[0-9]{7,12}"
    ### Get the folder path for the folder with the master UI copy ###
    folder_template = str(input("""Give the full file path to the folder with the UI you want to copy to other accounts! IE: C:/users/user/Desktop/eve_template
    
    >"""))

    ### Get the folder path for the folder with the UI's to copy over ###
    folder_replace = str(input("""Give the full file path to the folder with the UIs you want to replace! IE: C:/users/user/Desktop/eve_old_UIs
    
    >"""))

    ### Get the folder path for the updated files ###

    folder_destination = str(input("""Give the full file path to the folder you want to move the new UIs to! (Use a different folder then the preivous question! 
    IE: C:/users/user/Desktop/new_UIs
    
    >"""))

    ### Define the replacement IDs needed
#    replacement_char_IDs = []
#    replacement_user_IDS = []

    ### Get the source char and user ID's ###

    for filename in os.listdir(folder_template):
        if filename.startswith("core_char_") and not filename.startswith("core_char__"):
            char = re.search(regex_pattern, filename)
            template_char = str(char.group())
        elif filename.startswith("core_user_") and not filename.startswith("core_user__"):
            char = re.search(regex_pattern, filename)
            template_user = str(char.group())

### Find the IDs to replace and replace them into the new folder! ###

    for filename in os.listdir(folder_replace):
        if filename.startswith("core_char_") and not filename.startswith("core_char__"):
            char = re.search(regex_pattern, filename)
            copy_file = "{}\\core_char_{}.dat".format(folder_template, template_char)
            dest_file = "{}\\core_char_{}.dat".format(folder_destination, char.group())
            shutil.copy(copy_file, dest_file)

        elif filename.startswith("core_user_") and not filename.startswith("core_user__"):
            char = re.search(regex_pattern, filename)
            copy_file = "{}\\core_user_{}.dat".format(folder_template, template_user)
            dest_file = "{}\\core_user_{}.dat".format(folder_destination, char.group())
            shutil.copy(copy_file, dest_file)

main()
