#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip3 install pymysql')


# In[31]:


get_ipython().system('pip3 install boto3')


# In[3]:


import pandas as pd
from sqlalchemy import create_engine
import pymysql


# In[10]:


engine = create_engine("mysql+pymysql://user:password@url-database/dbname?charset=utf8mb4")


# In[16]:


sql = '''
    select * from sakila.rental rental
    inner join sakila.customer customer on rental.customer_id = customer.customer_id
    inner join sakila.inventory inventory on rental.inventory_id = inventory.inventory_id
    inner join sakila.staff staff on rental.staff_id = staff.staff_id
    inner join sakila.film film on inventory.film_id = film.film_id 
    inner join sakila.film_category film_category on film.film_id = film_category.film_id
'''


# In[17]:


df = pd.read_sql(sql, engine)


# In[18]:


df.head()


# In[19]:


df.columns


# In[26]:


df_final = df[['rental_id', 'rental_date', 'return_date', 'inventory_id', 'customer_id', 'store_id', 'first_name', 'last_name', 'email', 'staff_id', 'title', 'description', 'release_year']]


# In[ ]:





# In[27]:


df_final = df_final.dropna()


# In[28]:


df_final.dtypes


# In[30]:


df_final.isnull().sum()


# ### Save to S3

# In[32]:


from io import StringIO
import boto3


# In[38]:


s3_client = boto3.resource(
    's3',
    aws_access_key_id='acess_key_value',
    aws_secret_access_key='secret_access_key'
)


# In[43]:


bucket = 'teste-salvar-arquivos'
csv_buffer = StringIO()
df_final.to_csv(csv_buffer)
s3_client.Object(bucket, 'arquivos/df.csv').put(Body=csv_buffer.getvalue())


# In[ ]:




