import os 
import shutil 

def conditional_folder_on_demand(file_path, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    shutil.move(file_path, os.path.join(target_directory, os.path.basename(file_path)))