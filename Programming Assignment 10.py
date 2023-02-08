#!/usr/bin/env python
# coding: utf-8

# 1) Write a Python program to find sum of elements in list?

# In[2]:


l= [1,2,3,4,5,66,89,7]
sum=0
for i in l:
    sum=sum+i
print("sum of all the elements of list is", sum)


# 2) Write a Python program to Multiply all numbers in the list?

# In[3]:


l= [3,67,89,6,34]
m=1
for i in l:
    m=m*i
    
print("product of all the elements of the list is : ", m)    


# 3) Write a Python program to find smallest number in a list?

# In[4]:


l=[98,1234,666,56,3]
l.sort()
print("smallest number in the list is :", l[0])


# 4) Write a Python program to find largest number in a list?

# In[5]:


l=[98,1234,666,56,3]
l.sort(reverse=True)
print("Largest number in the list is :", l[0])


# 5) Write a Python program to find second largest number in a list?

# In[6]:


l=[98,1234,666,56,3]
l.sort(reverse=True)
print("Second Largest number in the list is :", l[1])


# 6) Write a Python program to find N largest elements from a list?

# In[10]:


l = [10,2398,3579,3100,200,-495,953]
n = 4

l.sort()
print(n, "largest numbers in the list is", l[-n:])


# 7) Write a Python program to print even numbers in a list?

# In[14]:


l = [10,2398,3579,3100,200,-495,953]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
print("Even numbers in the list are: ",l1)


# 8) Write a Python program to print odd numbers in a List?

# In[18]:


l= [34,66,71,23,11,3,68,90]
l1=[]
for i in l:
    if i%2!=0:
        l1.append(i)
print( "Odd numbers in the list are: ", l1)        


# 9) Write a Python program to Remove empty List from List?

# In[21]:


l=[12,333,560,[], 23,'shere', 'tickernessia',[]]
l1=[]
for i in l:
    if i!=[]:
        l1.append(i)
        
print("The new list is:", l1)        
        


# 10) Write a Python program to Cloning or Copying a list?

# In[22]:


def cloning_list(l1):
    l= l1[:]
    return l

l1=[1,2,3,4,5,6,7]
l=cloning_list(l1)
print("Original list is :", l1)
print("Cloned or copied list is :", l)
    


# 11) Write a Python program to Count occurrences of an element in a list?

# In[24]:


l1=[1,2,3,4,5,6,7,1,1,1,2,4,7]


def count_element_occurance(l1,x):
    count=0
    for i in l1:
        if i in l1:
            count=count+1
    return count

y=count_element_occurance(l1,1)
print("Count of ocuurance of the given number is: ", y)
        
        


# In[ ]:




