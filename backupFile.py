import shutil
import os
source=input("enter source")
dest=input("input destination")
source=source+"/"
dest=dest+"/"
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),dest)