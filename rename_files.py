import os
    
def rename_files ():
    #get file name from a folder
    file_list = os.listdir(r"D:\GitHub\Python-Practice\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is :" +saved_path)
    os.chdir("D:\GitHub\Python-Practice\prank")
    #for each file, rename it
    for file_name in file_list:
        print("Old name is :"+file_name)
        print("New name is : "+file_name.lstrip("0123456789"))
        os.rename(file_name,file_name.lstrip("0123456789"))
rename_files()
