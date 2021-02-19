#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys

for line in sys.stdin:
    line = line.strip()
    items = line.split()
    itemlen = len(items)
    #num1 stands for the position first item have when in the line
    for po1 in range(itemlen):
        po2 = po1 + 1
            for po2 in range(itemlen):
                if po2 >= po1+1:
                    print('(%s,%s)\t%s' % (items[po1], items[po2], 1))
                    po2+=1
                po2 += 1

    
        
        
    

