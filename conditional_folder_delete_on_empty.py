import os 
from remove_empty_folder import remove_empty_directory

def conditional_folder_delete_on_empty():
    os.makedirs('./still_images', exist_ok = False)
    os.makedirs('./audio', exist_ok = False)
    os.makedirs('./animation', exist_ok = False)

    remove_empty_directory('./animation')
