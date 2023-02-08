#!/usr/bin/env python
# coding: utf-8

# 1) Create an assert statement that throws an AssertionError if the variable spam is a negative
# integer.

# In[1]:


import pyinputplus as pyip

spam = pyip.inputNum(" Enter a positive number :")
assert spam > 0
print(spam,'is a positive number')


# 2) Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain
# strings that are the same as each other, even if their cases are different (that is, &#39;hello&#39; and &#39;hello&#39; are
# considered the same, and &#39;goodbye&#39; and &#39;GOODbye&#39; are also considered the same).

# In[2]:


eggs='Hello'
bacon ='hello'

assert eggs.lower() != bacon.lower() or eggs.upper() != bacon.upper()
print('The eggs and bacon variables are not same')


# 3) Create an assert statement that throws an AssertionError every time.

# In[4]:


assert False  # this statement always throws an error


# 4) What are the two lines that must be present in your software in order to call logging.debug()?

# In[5]:


import logging as log
log.basicConfig(level=log.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# 5) What are the two lines that your program must have in order to have logging.debug() send a
# logging message to a file named programLog.txt?

# In[6]:


import logging as log
log.basicConfig(filename='programLog.txt', level=log.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# 6) What are the five levels of logging?

# Five levels of logging are
# 
# 1) logging.info()   : used to confirm a program is running and general events
# 
# 2) logging.debug()  : variable's state and small details
# 
# 3) logging.warning() : potential problem to work on in the future
# 
# 4) logging.error()   : to record the errror at runtime
# 
# 5) logging.critical() : to record any fatal error
# 

# 7) What line of code would you add to your software to disable all logging messages?

# In[7]:


import logging as log
log.disable(log.CRITICAL)


# 8) Why is using logging messages better than using print() to display the same message?

# logging meassages stores the information or the data in a logging file which has numerous information related to errors, critical errors , warnings and also shows the time and date of execution which further helps in debugging as well

# 9) What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

#  Step in button will move the debugger into a function call. 
#  Step Over button will quickly execute the function call without stepping into it. 
#  Step Out button will quickly execute the rest of the code until it steps out of the function it currently is in.

# 10)After you click Continue, when will the debugger stop ?

# Debugger will stop at the next breakpoint if the code has no breakpoint it will be executed fully

# 11) What is the concept of a breakpoint?

# The breakpoint () function engages, configures, and changes the debugger program used in a script

# In[ ]:




