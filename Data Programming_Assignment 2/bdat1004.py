#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2.2 Write a program that uses input to prompt a user for their name and then welcomes them.
var1 = input('Enter your name: ');
print ("Hello " + var1);


# In[11]:


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


# In[12]:


try:
    hours = int(input("Enter hrs: "))
    rate = float(input("Enter rate: "))
    pay = hours*rate
    print("pay: ", pay)
except:
    print("Please Enter decimal data")


# In[2]:


hrs= input("Enter Hour:")
rate= input("Eenter Rate per Hour:")
pay= float(hrs)*float (rate)
print("Pay:", pay)


# In[3]:


hrs= input("Enter Hour:")
rate= input("Eenter Rate per Hour:")
pay= float(hrs)*float (rate)
print("Pay:", pay)


# In[16]:


def groot():
    print("Hiii")
def marvel():
    print("Heyyaa")
groot()
marvel()


# In[4]:


width = 17
height = 12.0
print width/2
print type(width/2)


# In[5]:


width = 17;
height = 12.0;
print (width/2);
print type(width/2);


# In[6]:


width = 17;
height = 12.0;
print (width/2);
print (type(width/2));


# In[7]:


width = 17;
height = 12.0;
print (width/2.0);
print (type(width/2.0));


# In[8]:


width = 17;
height = 12.0;
print (width//2);
print (type(width/2));


# In[9]:


width = 17;
height = 12.0;
print (height/3);
print (type(height/3));


# In[10]:


print (1 + 2 * 5);
print (type(1 + 2 * 5));


# In[ ]:


temp_Celcius = input('Enter a temp in Celcius: ')
temp_Farenheight = (float(temp_Celcius) * 1.8) + 32
print ('This is equivalent to '),
print temp_Farenheight,
print (' degrees Farenheight')

