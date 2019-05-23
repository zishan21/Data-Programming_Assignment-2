#!/usr/bin/env python
# coding: utf-8

# In[4]:


def computePay(hours,rate):
    #hours = int(input("Enter hours: "))
    #rate = input("Enter rate: ")
    if hours<=40:
        pay = hours*rate
        return pay
    else :
        ex_hours = hours - 40;
        ex_rate = rate*1.5;
        pay = 40*rate+ex_hours*ex_rate;
        return pay
x = computePay(int(input("hours: ")),float(input("rate: ")))
print(x)
    


# In[ ]:




