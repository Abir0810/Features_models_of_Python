#!/usr/bin/env python
# coding: utf-8

# # Extract Text from PDF using Python

# In[9]:


import PyPDF2
pdf=open("E:\Cover.pdf","rb")
reader=PyPDF2.PdfFileReader(pdf)
page=reader.getPage(0)
print(page.extractText())


# In[ ]:




