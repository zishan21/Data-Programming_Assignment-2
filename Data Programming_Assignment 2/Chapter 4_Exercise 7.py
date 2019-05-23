#!/usr/bin/env python
# coding: utf-8

# In[4]:


def computeGrade(score):


    
    if score>=1.0:
            return "please enter score between 0.0 and 1.0"
    elif score>=0.9:
            return "A"
    elif score>=0.8:
            return "B"
    elif score>=0.7:
            return "C"
    elif score>=0.6:
            return "D"
    else:
        return "F"
try:
    x = computeGrade(float(input("score: ")))
    print("Grade", x)
except:
    print("Enter valid score")


# In[ ]:





# In[ ]:





# In[ ]:




