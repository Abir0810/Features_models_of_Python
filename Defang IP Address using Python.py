#!/usr/bin/env python
# coding: utf-8

# # Defang IP Address using Python

# In[3]:


def ip_address(address):
    new_address=""
    split_address=address.split(".")
    separator="[.]"
    new_address=separator.join(split_address)
    return new_address
IPad= input("Enter your IP address: ")
ipaddress= ip_address(IPad)
print(ipaddress)


# In[ ]:




