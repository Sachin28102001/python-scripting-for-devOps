# Program to find all the files in a folder that a user gives.

import os 

# Input - list of folders name 

# Output - list of files in the provded folders.

folders=input("please provide the folder name with space in between:").split()

# for folder in folders:
#     list_of_files=os.listdir(folder)
#     print("--> list of files in a folder " + folder)   
    
# for file in list_of_files:
#     print(file) 


for folder in folders:
    
    try:
      files=os.listdir(folder)     
    except FileNotFoundError:
        print("The folder does not exist - " + folder)
        break
        
    print("--> list of files in a folder " + folder)   
    
for file in files:
    print(file)