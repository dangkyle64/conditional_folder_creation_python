import os 

def remove_empty_directory(path_to_directory):
    if not os.listdir(path_to_directory):
        os.rmdir(path_to_directory)
        print(f"Directory '{path_to_directory}' removed successfully")
    else:
        print(f"Directory '{path_to_directory}' is not empty")

def clear_folders():
    remove_empty_directory('./still_images')
    remove_empty_directory('./audio')
    remove_empty_directory('./animation')