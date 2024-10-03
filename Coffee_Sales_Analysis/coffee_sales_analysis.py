#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings


# In[3]:


warnings.filterwarnings('ignore')


# In[13]:


# Accessing Datafile
df = pd.read_csv(r"C:\Users\Sushant\Downloads\index.csv")


# In[14]:


# Data pre-processing
df.info()


# In[27]:


df.head(5)


# In[29]:


# Shape of the data
df.shape 


# In[16]:


# Checking for duplicates
df.duplicated().sum()


# In[17]:


# Checking for null values 
df.isnull().sum()


# In[18]:


# Checking for data types
df.dtypes


# In[19]:


# Typecasting (coversion of data types)
df['date'] = pd.to_datetime(df['date'])
df['datetime'] = pd.to_datetime(df['datetime'])


# In[24]:


# Statistical overview 
df['money'].describe()


# In[26]:


df.loc[:,['cash_type', 'card', 'coffee_name']].describe()


# - There are 1133 records and 6 columns in the dataset.
# - 2 unique values of 'cash types'.
# - 8 different 'coffee types'.
# - 'Americano with Milk' is the most popular product.
# - 89 missing values in the column card.
# - Most of the people use this card type 'ANON-0000-0000-0012'

# In[ ]:





# In[69]:


# cash_type value counts 
cash_type_counts = df['cash_type'].value_counts(normalize=True)*100


# In[74]:


# Histogram for analyzing cash type
plt.figure(figsize=(4,3))
plt.pie(cash_type_counts, labels = cash_type_counts.index, autopct = '%1.1f%%', startangle=180)
plt.axis('equal')
plt.title('Pie Chart for cash type')
plt.show()


# In[75]:


df['cash_type'].value_counts(normalize = True)*100


# - 92.14% of the transactions are from card users.

# In[57]:


pd.DataFrame(df['coffee_name'].value_counts(normalize=True).sort_values(ascending=False).round(4)*100).T


# - 'Americano with Milk' and 'Latte' are the most popular coffee products. And covers 45% of the sales.
# - While 'Cortado', 'Hot Chocolate', 'Espresso' and 'Cocoa' are less popular. And covers only 24% sales.

# In[58]:


# Creating some new columns for timeseries analysis of sales
df['month'] = df['date'].dt.strftime('%Y-%m')
df['day'] = df['date'].dt.strftime('%w')
df['hour'] = df['datetime'].dt.strftime('%H')


# In[59]:


df.info()


# In[60]:


df.head()


# In[61]:


df['date'].min(), df['date'].max()


# - The time range of this data set is from '2024-03-01' to '2024-07-31'

# In[92]:


revenue_data = df.groupby(['coffee_name']).sum(['money']).reset_index().sort_values(by='money',ascending=False)


# In[134]:


# Frequency count of each coffee name
print(df['coffee_name'].value_counts())
      
# Plotting the distribution of coffee names
plt.figure(figsize=(5, 3))
ax = sns.barplot(data=revenue_data,x='money',y='coffee_name', color='steelblue')
ax.bar_label(ax.containers[0], fontsize=6)
plt.title('Revenue by Products')
plt.xlabel('Revenue')
plt.show()


# - Latte is the product with highest revenue, while Espresso is the least popular product.

# In[140]:


# Grouping the data by coffee type and month, counting the number of sales (using 'date' as a proxy for transactions)
monthly_sales = (df.groupby(['coffee_name', 'month'])['date'].count().reset_index()
                 .rename(columns={'date': 'count'}).pivot(index='month', columns='coffee_name', values='count').reset_index())  

# Display the transformed monthly sales DataFrame
monthly_sales


# In[176]:


monthly_sales.describe().T.loc[:,['min', 'max', 'mean']]


# In[161]:


plt.figure(figsize=(7,4))
sns.lineplot(data=monthly_sales)
plt.legend(loc='upper left', fontsize=(6))
plt.xticks(range(len(monthly_sales['month'])),monthly_sales['month'],size='small')
plt.title('Monthly Sales by Products')
plt.show()


# - The above line chart shows, 'Americano with Milk' and 'Latte' are top selling products and showing an upward trend.
#   While 'Cappuccino' is top selling but showing an down trend.
# - 'Cocoa' and 'Espresso' are least sold products.

# In[164]:


weekday_sales = df.groupby(['day']).count()['date'].reset_index().rename(columns={'date':'count'})
weekday_sales.T


# In[170]:


plt.figure(figsize=(5,3))
sns.barplot(data=weekday_sales,x='day',y='count',color='steelblue')
plt.xticks(range(len(weekday_sales['day'])),['Sun','Mon','Tue','Wed','Thur','Fri','Sat'],size='small')
plt.title('Weekday Sales by Products')
plt.show()


# - As above chart shows, Tuesday has the highest sales of the week, while the sales are on other days are similar.

# In[173]:


daily_sales = (df.groupby(['coffee_name','date']).count()['datetime']
               .reset_index().reset_index().rename(columns={'datetime':'count'})
               .pivot(index='date',columns='coffee_name',values='count').reset_index().fillna(0))
daily_sales.head(5)


# In[175]:


daily_sales.iloc[:,1:].describe().T.loc[:,['min','max', 'mean']]


# - This table shows the daily sales.

# In[181]:


hourly_sales = df.groupby(['hour']).count()['date'].reset_index().rename(columns={'date':'count'})
hourly_sales.head(6)


# In[197]:


plt.figure(figsize=(4,3))
sns.barplot(data=hourly_sales,x='hour',y='count',color='steelblue')
plt.title('Hourly Sales Analysis')
plt.show()


# - Overall, three peak hours within each day can be observed: 10:00am, 11:00am and 7:00pm. 
# Then, let's check if any difference for different products.

# In[189]:


hourly_sales_by_coffee = (df.groupby(['hour','coffee_name']).count()['date'].reset_index().rename(columns={'date':'count'})
                          .pivot(index='hour',columns='coffee_name',values='count').fillna(0).reset_index())
hourly_sales_by_coffee.head()


# - The above chart shows that hour by hour sales followed by coffee types.

# In[200]:


# Customers who purchased coffee more than once.
# Finding returning card customers
returning_customers = df['card'].value_counts()
returning_customers = returning_customers[returning_customers > 1].index
returning_customers_df = df[df['card'].isin(returning_customers)]
returning_customers_count = returning_customers_df['card'].value_counts()
returning_customers_count = returning_customers_df['card'].nunique()
casual_customers_count = df['card'].nunique() - returning_customers_count

# Prepare the data for plotting
customer_counts = pd.Series([returning_customers_count, casual_customers_count],
                            index=['Returning Customers', 'Casual Customers'])

# Plotting pie chart returning card customers
plt.figure(figsize=(6, 4))
customer_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='Set3')
plt.title('Percentage of Transactions by Returning Card Customers')
plt.ylabel('')
plt.show()


# In[ ]:




