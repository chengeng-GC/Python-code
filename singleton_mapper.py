#!/usr/bin/env python
# coding: utf-8

# In[10]:


import sys


# In[9]:


#get all lines from stdin
for line in sys.stdin:
    #strip()函数
    #用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    #注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    #strip()方法语法：
    #str.strip([chars]);
    #参数-chars -- 移除字符串头尾指定的字符序列。
    line=line.strip()
    #split()函数
    #语法：str.split(str="",num=string.count(str))[n]
    #参数说明：
    #str：表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素。
    #num：表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量。
    #[n]：表示选取第n个分片
    #注意：当使用空格作为分隔符时，对于中间为空的项会自动忽略。
    items=line.split()
    #output (item,1) in tab-delimited format
    for item in items:
        print('(%s)\t%s' % (item,1))
    


# In[ ]:




