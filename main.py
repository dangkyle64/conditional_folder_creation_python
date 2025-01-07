from conditional_folder_delete_on_empty import conditional_folder_delete_on_empty
from conditional_folder_on_demand import conditional_folder_on_demand

def main():
    conditional_folder_delete_on_empty()
    conditional_folder_on_demand('text1.txt', './animation')

main()
