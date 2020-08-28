#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv
import time
import datetime as dt
import matplotlib.pyplot as plt
from datetime import datetime


# In[2]:


read_file = pd.read_excel (r"/Users/user/Downloads/tourism_data4.xlsx")
read_file.to_csv (r"/Users/user/Downloads/tourism data.csv", index = None, header=True)
df_tourism = pd.read_csv (r"/Users/user/Downloads/tourism data.csv")

df_tourism.head()


# In[3]:


for month in df_tourism.columns[1:]:
    
            df_tourism = df_tourism.sort_values([month], ascending=[False])
            plt.rcParams['figure.figsize'] = (20,15) 
            fig, ax = plt.subplots()
            fig.autofmt_xdate()
            plt.ylabel('Number of Tourists Entering Singapore', fontsize=20)
            plt.ylim(0, 700000)
            plt.xticks(fontsize=16)
            plt.yticks(fontsize=16)
            plt.bar(df_tourism['countries'], df_tourism[month])
            df = pd.to_datetime('{}'.format(month))
            title = df.strftime('%b %Y')
            plt.title(title, x=0.7, y=0.8, fontsize=100)
            filename = df.strftime('tourism%Y%m')
            plt.savefig(f'tourism_graphs/{filename}.png', dpi=500)
            plt.show()
 
    
            
  
    
    


# In[ ]:


from PIL import Image
import glob

# Create the frames
frames = []
imgs = glob.glob("tourism_graphs/*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# Save into a GIF file that loops forever
frames[0].save('tourism.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)


# In[ ]:




