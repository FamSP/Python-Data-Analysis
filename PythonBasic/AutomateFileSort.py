import os, shutil 

path = r"C:/Users/tame_/OneDrive/Desktop/Data Analyst/tableau/"


folder_name = ['csv file', 'image file' , 'text file']

for loop in range(0,3):
    if not os.path.exists(path + folder_name[loop]):
        os.makedirs(path + folder_name[loop])
# print(check)

file_name = os.listdir(path)

for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv file/" + file):
        shutil.move(path + file,path + "csv file/"+ file)