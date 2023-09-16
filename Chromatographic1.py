#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


# In[2]:


read_csv = r'chromatographicData.csv'
data = pd.read_csv(read_csv,skiprows=[0,1,2,10,11])


# In[3]:


data1 = data.loc[0:4]
data1


# In[4]:


data1.columns


# In[ ]:





# In[12]:


data1.plot.line(x='Retention Time',y=['Raw MS1 Scan Abundance','Fitted Gaussian','1061.416232'],marker='o')
plt.title('Chromatographic Data1')
plt.show()


# In[6]:


data2 = pd.read_csv(read_csv,skiprows=np.arange(0,11,1))
data2


# In[7]:


data2.columns


# In[14]:


data2.plot.line(x='Retention Time', y=['Raw MS1 Scan Abundance','Fitted Gaussian','1061.920759'], marker='o')
plt.title('Chromatograhic Data2')
plt.show()


# In[ ]:




