#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings 


# In[2]:


warnings.filterwarnings('ignore')


# In[3]:


# Importing dataset
df = pd.read_csv(r"C:\Users\Sushant\Downloads\netflix1.csv")


# In[4]:


df.head()


# In[15]:


df.info()


# In[17]:


df.duplicated().sum()


# In[19]:


df.isnull().sum()


# In[20]:


df.dtypes


# In[22]:


df.shape


# - There are no duplicates in the dataset.
# - There are no missing values in the dataset.
# - This dataset contains 10 columns and 8790 rows.
# - There are some irrelenvant types, let's convert them.

# In[27]:


# typecasting (converting data types)
df['date_added'] = pd.to_datetime(df['date_added'])
df['release_year'] = pd.to_datetime(df['release_year'])


# In[46]:


types = df['type'].value_counts(normalize=True)*100
types


# In[50]:


plt.figure(figsize=(4,3))
plt.pie(types, labels=types.index, autopct='%1.1f%%', startangle=180)
plt.axis('equal')
plt.title('Types of Show')
plt.show()


# - From the above Pie chart we can see that the 70% of people watch movies and rest 30% watch TV shows.

# In[51]:


# Rating of TV shows and Movies
df['rating'].value_counts()


# In[58]:


# Ratings 
ratings = df['rating'].value_counts().reset_index().sort_values(by='count', ascending=False)

plt.figure(figsize=(5,3))
plt.bar(ratings['rating'], ratings['count'])
plt.xticks(rotation=45, ha='right')
plt.xlabel('Rating Types')
plt.ylabel('Rating Frequency')
plt.title('Rating on Netfilx')
plt.show()


# - From the above chart we can observe that the 'TV-MA' and 'TV-14' having the highest rating frequency.
# - While 'TV-Y7-FV', 'NC-17' and 'UR' types having least rating frequencies.

# In[68]:


top_10_countries = df['country'].value_counts().reset_index().sort_values(by= 'count', ascending= False).head(10)
top_10_countries.T


# In[79]:


# Graphical representation 
plt.figure(figsize=(5,3))
plt.bar(top_10_countries['country'], top_10_countries['count'])
plt.xticks(rotation=45, ha='right')
plt.xlabel('Country')
plt.ylabel('Frequency')
plt.title('Top 10 Countries with most content on Netflix')
plt.show()


# - The above analysis shows that graphical representation of Top 10 Countries with content highest content frequency on Netflix.

# In[86]:


# Movie genre analysis.
movie_genre = df[df['type']=='Movie'].groupby('listed_in').size().sort_values(ascending=False).head(10)
movie_genre


# In[89]:


# Bargraph for movie genre.
plt.figure(figsize=(5,4))
plt.bar(movie_genre.index, movie_genre.values)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.title('Top 10 Genres for Movies')
plt.show()


# - Above graph describes that the frequency of movies by Top 10 Genres.
# - Dramas, International Movies and Documentaries are most.

# In[ ]:


# TV genre analysis
series_genre = df[df['type']=='TV Show'].groupby('listed_in').size().sort_values(ascending=False).head(10)
series_genre


# In[93]:


plt.figure(figsize=(5,4))
plt.bar(series_genre.index, series_genre.values)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Genre')
plt.ylabel('TV shows Frequency')
plt.title('Top 10 TV Shows by Genre')
plt.show()


# In[103]:


# Top 10 Directors
top_10_directors = df['director'].value_counts().reset_index().sort_values(by='count', ascending=False)[1:10]
top_10_directors


# In[104]:


plt.figure(figsize=(5,4))
plt.bar(top_10_directors['director'], top_10_directors['count'])
plt.xticks(rotation='vertical', ha='right')
plt.xlabel('Director_names')
plt.ylabel('Count')
plt.title('Top 10 Directors with highest Shows')
plt.show()


# In[107]:


# Creating some more columns of date for yearly, monthly and weekly analysis.
import datetime as dt
df['year'] = df['date_added'].dt.year
df['month'] = df['date_added'].dt.month
df['day'] = df['date_added'].dt.day


# In[108]:


df.info()


# In[114]:


yearly_movie_release = df[df['type']== 'Movie']['year'].value_counts().sort_index()

yearly_series_release = df[df['type']=='TV Show']['year'].value_counts().sort_index()

plt.plot(yearly_movie_release.index, yearly_movie_release.values, label = 'Movies')
plt.plot(yearly_series_release.index, yearly_series_release.values, label = 'Series')
plt.xlabel('Years')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.title('Distribution of Yearly releases of Shows and Movies')
plt.show()


# In[116]:


# Monthly release analysis
monthly_movie_release=df[df['type']=='Movie']['month'].value_counts().sort_index()
monthly_series_release=df[df['type']=='TV Show']['month'].value_counts().sort_index()

plt.plot(monthly_movie_release.index, monthly_movie_release.values, label='Movies')
plt.plot(monthly_series_release.index, monthly_series_release.values, label='Series')
plt.xlabel("Months")
plt.ylabel("Frequency of releases")
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.grid(True)
plt.suptitle('Monthly releases of Movies and TV shows')
plt.show()


# - The above line chart shows that the frequency of yearly release of 'Movies' was at peak between 2018-19 and suddenly shows some downtrend in 2020.
# - While the monthly release of 'Movies' records high frequency of 550.
# - Hence we can observe that release of 'Movies' are more than the 'Series'.

# In[124]:


df.to_csv('Netflix_cleaned.csv', index=False)


# In[ ]:




