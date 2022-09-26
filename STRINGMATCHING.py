#!/usr/bin/env python
# coding: utf-8

# In[1]:


def string_match(string,substring):
    temp=len(string)
    temp1=len(substring)/3 #length of the substring(pattern)
    for a in range(int(temp-temp1+1)):
        b=0
        while(b<temp1):
            if string[a+b]==substring[b]:
                b+=1
            else:
                break
    
            print('found at position',a)


# In[7]:


string_match("jncbcbvsnadkfjknefkthewyonkf", "the")


# In[ ]:





# In[ ]:




