#!/usr/bin/env python
# coding: utf-8

# # Real-time Currency Converter With Python

# In[3]:


from forex_python.converter import CurrencyRates
c= CurrencyRates()
amount=int(input("Enter the ammount: "))
from_currency= input("From Currency:").upper()
to_currency=input("To Currency: ").upper()
print(from_currency,"To",to_currency,amount)
result=c.convert(from_currency,to_currency,amount)
print(result)


# In[ ]:




