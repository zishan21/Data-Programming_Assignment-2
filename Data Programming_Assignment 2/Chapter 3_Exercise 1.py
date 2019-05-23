#!/usr/bin/env python
# coding: utf-8

# In[12]:


hours = input("Enter hours: ");
hours=int(hours);
rate = input("Enter rate: ");
rate= float(rate);

if hours<=40:
    pay = hours*rate;
    print("Pay: ", pay);
else :
    ex_hours = hours - 40;
    ex_rate = rate*1.5;
    pay = 40*rate+ex_hours*ex_rate;
    
    print("Pay: ", pay);
    


# In[ ]:




