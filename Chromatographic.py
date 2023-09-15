#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


# In[23]:


read_csv = r'chromatographicData.csv'
data = pd.read_csv(read_csv,skiprows=[0,1,2,10,11])


# In[29]:


data1 = data.loc[0:4]
data1


# In[33]:


data1.columns


# In[ ]:





# In[34]:


data1.plot.line(x='Retention Time', y=['Raw MS1 Scan Abundance', 'Fitted Gaussian',
       '1061.416232'], marker='o')


# In[30]:


data2 = pd.read_csv(read_csv,skiprows=np.arange(0,11,1))
data2


# In[31]:


data2.columns


# In[38]:


data2.plot.line(x='Retention Time', y=['Raw MS1 Scan Abundance','Fitted Gaussian','Raw MS1 Scan Abundance', 'Fitted Gaussian',
       '1061.416427', '1061.920759'], marker='o')

