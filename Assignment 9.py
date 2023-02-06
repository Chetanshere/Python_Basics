#!/usr/bin/env python
# coding: utf-8

# 1) To what does a relative path refer?

# A relative path refers to a location that is relative to a current directory. Relative paths make use of two special symbols, a dot (.) and a double-dot (..), which translate into the current directory and the parent directory. Double dots are used for moving up in the hierarchy.

# 2) What does an absolute path start with your operating system?

# The absolute path of a file is specified starting with a drive letter, followed by the hierarchy of directories in which the file is contained (with each directory separated by a backslash), and concluding with the exact filename.

# 3) What do the functions os.getcwd() and os.chdir() do?

# os.getcwd()=This method returns a string which represents the current working directory.
# 
# os.chdir()= This method is used to cjange the current directory.

# 4) What are the . and .. folders?

# . single dot represents current directory while we use .. to access the current directory 

# 5) In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

# Dir name is C:/\bacon/\eggs/, base name is spam.txt.

# 6) What are the three “mode” arguments that can be passed to the open() function?

# Read mode: open('test.txt', 'r'), Write mode: open('test.txt', 'w'), Append mode: open('test.txt', 'a').

# 7) What happens if an existing file is opened in write mode?

# It will overwrite the existing file and start from scratch

# 8) How do you tell the difference between read() and readlines()?

# read() returns all the content as a single string value while readline() method gets the list of string values from the file

# 9) What data structure does a shelf value resemble?

# it resembles dictionary data structure 

# In[ ]:




