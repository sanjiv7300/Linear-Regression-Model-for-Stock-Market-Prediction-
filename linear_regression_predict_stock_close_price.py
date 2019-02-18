#!/usr/bin/env python
# coding: utf-8

# In[46]:


# This Linear Regression model for Stock Market Predecting 

import pandas_datareader.data as web # import pandas_datareader to read data from the web - stock market 
import datetime as dt 
import pandas as pd
import matplotlib.pyplot as plt  # for ploting the graph 
from sklearn import linear_model  # linear regression in built math function - y= mx+ b  


# In[39]:


start = dt.datetime(2018,11,17)
end = dt.datetime.today()
stock = 'DHFL.NS'       
df = web.DataReader(stock,'yahoo',start, end) # reading the data from web - yahoo fin
print(df.head()) 


# In[27]:


df = df.rename(columns = {'Adj Close':'CLOSE'})   # rename the Adj Close to Close 
print(df.tail())


# In[28]:


data_source = r'E:\Data_Set\DHFL.xlsx'   # writing the web data into excel 
df.to_excel(data_source)
df = pd.read_excel(data_source)       # reading the dataframe 


# In[29]:


print(df.tail())


# In[30]:


df = pd.read_excel(data_source, index_col = 'Date')     # changing the data to index coloum 
print(df.head())


# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline                # ploting the graph')
plt.xlabel('Opening Price')
plt.ylabel('Closing Price')           
plt.scatter(df.Open, df.CLOSE)        # open: independent variable  close: depedent variable 


# In[32]:


reg = linear_model.LinearRegression()       # calling linear regression 
reg.fit(df[['Open']], df.CLOSE              # passing the variables to the model  independent,  dependent


# In[33]:


today_open_price = 124.900002                 # is the value of x in the formula 

predict_today_close_price = reg.predict([[today_open_price]])   #  predicting the value


# In[42]:


reg.intercept_                   # is the value of b in the formula  


# In[43]:


reg.coef_                      # is the value of m in the formula 


# In[44]:


print('Predicted todays close price:' , predict_today_close_price) # predicted value  is y in the formula 


# In[47]:


(0.97596752 * 124.900002) + 3.285443530585411       # y = m x + b


# In[ ]:


# This linear Regression Model is only a example for Bigners 

