import os
import shutil
path=input("enter the path to be organised")
listoffiles=os.listdir(path)
for file in listoffiles:
    name,ext = os.path.splitext(file)
    ext=ext[1:]
    if ext=="":
        countinue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)