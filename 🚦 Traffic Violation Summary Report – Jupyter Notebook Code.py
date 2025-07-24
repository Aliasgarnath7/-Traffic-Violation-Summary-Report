#!/usr/bin/env python
# coding: utf-8

# # Visual Analysis on Traffic Violation

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[2]:


itv = pd.read_csv("Indian_Traffic_Violations.csv")


# In[3]:


itv.head()


# In[4]:


itv.shape


# In[5]:


itv.info()


# In[6]:


itv.isnull().sum()


# In[7]:


itv.duplicated().sum()


# In[8]:


itv.describe()


# In[9]:


# Convert time column to datetime if available
if 'Time' in itv.columns:
    itv['Time'] = pd.to_datetime(itv['Time'], errors='coerce')
    itv['Hour'] = itv['Time'].dt.hour

# Check for nulls
itv.isnull().sum()


# # Top 10 Locations with Most Violations

# In[10]:


if 'Location' in itv.columns:
    location_violations = itv['Location'].value_counts().nlargest(10)

    plt.figure(figsize=(10,6))
    sns.barplot(x=location_violations.values, y=location_violations.index, palette='Reds_r')
    plt.title("Top 10 Locations with Most Violations")
    plt.xlabel("Number of Violations")
    plt.ylabel("Location")
    plt.show()


# # Top 10 Types of Violations

# In[11]:


if 'Violation_Type' in itv.columns:
    type_violations = itv['Violation_Type'].value_counts().nlargest(10)

    plt.figure(figsize=(10,6))
    sns.barplot(x=type_violations.values, y=type_violations.index, palette='Blues_r')
    plt.title("Top 10 Types of Violations")
    plt.xlabel("Count")
    plt.ylabel("Violation Type")
    plt.show()


# # Violations by Hour of Day

# In[12]:


if 'Hour' in itv.columns:
    hourly = itv['Hour'].value_counts().sort_index()

    plt.figure(figsize=(10,6))
    sns.lineplot(x=hourly.index, y=hourly.values, marker='o')
    plt.title("Violations by Hour of Day")
    plt.xlabel("Hour of Day (0-23)")
    plt.ylabel("Number of Violations")
    plt.xticks(range(0,24))
    plt.grid(True)
    plt.show()


# In[17]:


print("🔍 Summary of Key Insights:\n")

if 'Location' in itv.columns:
    print("Top Violation Location:", itv['Location'].value_counts().idxmax())

if 'Violation_Type' in itv.columns:
    print("Most Common Violation Type:", itv['Violation_Type'].value_counts().idxmax())

if 'Hour' in itv.columns:
    print("Peak Violation Hour:", itv['Hour'].value_counts().idxmax())


# In[ ]:




