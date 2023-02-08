#!/usr/bin/env python
# coding: utf-8

# 1) How do you distinguish between shutil.copy() and shutil.copytree()?

# shutil.copy() : copies a single file
#     
# shutil.copytree() : copies an entire folder   

# 2) What function is used to rename files?

# file.rename() is used to rename the files

# 3) What is the difference between the delete functions in the send2trash and shutil modules?

# send2trash will move a ﬁle or folder to the recycle bin, shutil will permanently delete ﬁles and folders

# 4)ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is
# equivalent to File objects’ open() method?

# in zipfile method the files are open temporarily while in file objects open() method files are open permanently 

# 5) Create a programme that searches a folder tree for files with a certain file extension (such as .pdf
# or .jpg). Copy these files from whatever location they are in to a new folder.

# In[2]:


import os, shutil

def selectiveCopy(source, extensions, destFolder):
    folder = os.path.abspath(source)
    destFolder = os.path.abspath(destFolder)
    print('Looking in', source, 'for files with extensions of', ', '.join(extensions))
    for foldername, subfolders, filenames in os.walk(source):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
                fileAbsPath = foldername + os.path.sep + filename
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.mp4', '.pdf','.jpg']
source = "C:\\Users\\Chetanshere\\Desktop\\source"
destFolder = "C:\\Users\\Chetanshere\\Desktop\\dest"
selectiveCopy(source, extensions, destFolder)


# In[ ]:




