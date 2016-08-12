import os
import string

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir("/Users/partokarwat/Desktop/prank")

    saved_path = os.getcwd()
    os.chdir("/Users/partokarwat/Desktop/prank")

    #(2) for each file, rename file
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.strip("0123456789"))
        os.renames(file_name, file_name.strip("0123456789"))

    os.chdir(saved_path)
    
rename_files()
