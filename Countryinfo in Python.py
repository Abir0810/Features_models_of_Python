#!/usr/bin/env python
# coding: utf-8

# # Country Info in Python

# In[3]:


from countryinfo import CountryInfo
count=input("Enter your country: ")
country= CountryInfo(count)
print("Capital is :  ",country.capital())
print("Cureencies is : ",country.currencies())
print("languages is :   ",country.languages())
print("region is: ",country.region())
print("Population is: ",country.population())


# In[ ]:




