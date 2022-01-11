#!/usr/bin/env python
# coding: utf-8

# In[1]:


#first we are importing all the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#to ignore the warnings
import warnings as wg


# In[3]:


#now trun the cvv file(data set)
df=pd.read_csv('globalterrorismdb_0718dist.csv',encoding='latin',low_memory=False)
df.head() #for frist 5 data


# In[5]:


#over-all information about the data
df.info()


# In[6]:


df.shape


# In[7]:


#varifying the column inside the dataset
df.columns


# In[9]:


df.columns.values


# In[8]:


df.describe()


# In[11]:


df.corr()


# In[12]:


df.isnull().sum()


# In[13]:


df.duplicated().sum()


# In[15]:


#Number of unique value in each column

for i in df.columns:
    print (i,len(df[i].unique()))


# In[16]:


df.hist(figsize=(35,40))
plt.show()


# In[17]:


sns.set(rc={'figure.figsize':(25,40)})
sns.countplot(x=df['iyear'],hue =df['region_txt'])
plt.title('Region-wise terrorist activity in each year')


# In[19]:


#A more graph for better understaning region vise terrorist attacks in each year
# or you can use pd.crosstab(df.iyear,df.region_txt)
pd.crosstab(df['iyear'],df['region_txt']).plot(kind='line',figsize=(15,20))
plt.title('region-wise terrorist activity in each year')
plt.ylable('Number of Attacks')
plt.xlable('Years')
plt.show()

print('Middle east & North Africa has been reported to have more incident')


# In[20]:


#Most affected region
df['region_txt'].value_counts()


# In[21]:


df['country_txt'].value_counts()


# In[22]:


plt.figure(figsize=(15,6))
sns.barplot(df['country_txt'].value_counts()[:10].index,df['country_txt'].value_counts()[:10].values)
plt.title('Top 10 countries affected by Attacks', fontsize=15)
plt.ylable('Counts',fontsize=15)
plt.xlable('Countries',fontsize=15)
plt.show()

print('Most effected country is Iraq & mostly belongs to asia continent')


# In[26]:


plt.figure(figsize=(15,6))
sns.barplot(df['city'].value_counts()[:10].index,df['country_txt'].value_counts()[:10].values)
plt.title('Top 10 city affected by Attacks', fontsize=15)
plt.ylable('Counts',fontsize=15)
plt.xlable('City',fontsize=15)
plt.show()

print('Most effected city is baghdad & unknown')


# In[27]:


sns.set(rc={'figure.figsize':(30,7)})
sns.countplot(x=df['region_txt'],hue=df['weaptype1_txt'])
plt.title('Weapon type used in per region')
plt.xlable('Region',fontsize=15)
print('Explosives,chemicals and firearms are widely used as as weapon type')


# In[28]:


sns.set(rc={'figure.figsize':(30,7)})
sns.countplot(x=df['region_txt'],hue=df['attacktype1_txt'])
plt.title('Attack type used in per region')
plt.xlable('Region',fontsize=15)
print('Bombing/Explosion is highly used attack type and region in middle east/North asia')


# In[33]:


sns.set(rc={'figure.figsize':(30,10)})
sns.countplot(x=df['region_txt'],hue=df['targtype1_txt'])
plt.title('Attack type used in per region')
plt.xlable('Region',fontsize=15)
print('Private citizen/property is highly target type in each region')


# In[36]:


#Death and injuries at all the time 

df.plot(kind='scatter',x='nkill',y='nwound',color='green',figsize=(10,10),fontsize=15)
plt.xlabel('Kill')
plt.ylabel('Wound')
plt.title('kill-wound scatter plot')
plt.show()


# In[37]:


#Now ve are going to analysis the data of india

new=df[df['country_txt']=='India']['city']
new.value_counts()
#Most effected city of india-sri-nagar


# In[38]:


plt.figure(figsize=(10,15))
sns.barplot(new.value_counts()[:10].index,new.value_counts()[:10].values)
plt.title('Top 10 Terrorism effected city in india')
plt.ylable('City',fontsize=15)
plt.xlable('Attacks',fontsize=15)
plt.show()


# In[40]:


new=df[df['country_txt']=='India'][['city','iyear','attacktype1_txt','gname']]
new[:10]


# In[42]:


df['iyear'].value_counts()[:10]


# In[43]:


#Top terrorism group

df['gname'].value_counts()[:10]


# In[44]:


new=df[df['country_txt']=='India']['gname']
new.value_counts()


# In[45]:


new=df[df['country_txt']=='India']['iyear']
new.value_counts()


# In[48]:


new=df[df['country_txt']=='India']['attacktype1_txt']
new.value_counts()


# In[ ]:




