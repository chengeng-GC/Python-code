#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to 330740Large Scale Computing")


# In[2]:


myint = 330740
print(myint)
myfloat = 3.1415
print(myfloat)


# In[3]:


myFirstString = '330740'
print(myFirstString)
mySecondString = "Hadoop"
print(mySecondString)


# In[6]:


addition = myint + myfloat
print(addition)
subtraction = myint - myfloat
print(subtraction)
multiplication = myint * myfloat
print(multiplication)
division = myint / myfloat
print(division)
mod = myint % myfloat
print(mod)
concatenate1 = myFirstString + mySecondString
print(concatenate1)


# In[7]:


intList = [330, 740]
stringList = []
stringList.append("large")
stringList.append("scale")
stringList.append("computing")
print(intList[0])
print(intList[1])
print(stringList)


# In[8]:


name = "John"
age = 23
print(name == "John")
print(age > 25)
score = 85
if score >= 90:
 print("A")
elif score >=80:
 print("B")
else:
 print("C")


# In[9]:


for x in range(5):
 print(x)
for x in stringList:
 print(x)


# In[14]:


def convert2letter(totalScore):
 if totalScore >= 90:
     return "A"
 elif totalScore >= 80:
     return "B"
 else:
     return "C"
johnScore = 80
print(convert2letter(johnScore))


# In[16]:


print("Integer: %d" % myint)
print("Float: %f" % myfloat)
print("First element of stringList: %s" % stringList[0])
print("intList has %d elements, and the last element is %d" % (len(intList),intList[-1]))


# In[17]:


scoreBook={}
scoreBook["John"]=80
scoreBook["Jack"]=75
scoreBook["Jill"]=92
print("Jack receives %s from my course" % 
convert2letter(scoreBook["Jack"]))
print("Jill receives %s from my course" % 
convert2letter(scoreBook["Jill"]))


# In[ ]:




