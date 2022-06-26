#!/usr/bin/env python
# coding: utf-8

# # Contact Book in Python

# In[ ]:


names=[]
phone_numbers=[]
num=int(input("Enter number you want to save : "))
for i in range(num):
    name=input("Name: ")
    phone_number=input("Phone number: ")
    names.append(name)
    phone_numbers.append(phone_number)
print("\nName\t\t\tPhone number\n")
for i in range(num):
    print("{}\t\t\t{}".format(names[i],phone_numbers[i]))
search_term=input("\nEnter search term: ")
print("Search result:")
if search_term in names:
    index= names.index(search_term)
    phone_number= phone_numbers[index]
    print("Name: {}, phone number: {} ".format(search_term,phone_number))
else:
    print("Name not found")

