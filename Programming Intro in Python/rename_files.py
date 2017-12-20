import os
def rename_files():
    #(1) get file names
    
    file_list = os.listdir(r"/Users/See/Downloads/target file")
    print (file_list)
    saved_path = os.getcwd()
    
    #(2) rename file names
    for file_name in file_list:
        os.rename(file_name, file_list.translate(None, "0123456789"))
    
rename_files()
