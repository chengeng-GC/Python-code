#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
itemCount = {}
support = 2


# In[9]:


for line in sys.stdin:
    line = line.strip()
     #parse the key,value from mapper
    item, count = line.split('\t',1)
     #convert count from string to int
    try:
        count = int(count)
    except ValueError:
        #if count is not a number, ignore this line
        continue 
    #if item already in the dictionary, add the count
    try:
        itemCount[item] = itemCount[item]+count
    #otherwise, create a new key,value in dictionary
    except:
        itemCount[item] = count


# In[10]:


#output the desired items
for item in itemCount.keys():
    if itemCount[item] >= support:
        print('%s\t%s' % (item, itemCount[item]))


# In[ ]:





# In[ ]:




