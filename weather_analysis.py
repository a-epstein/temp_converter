#%% [markdown]
# # Weather Analysis for Edinburgh and New York 
#%% [markdown]
# ## Import libraries and csv containing dataset

#%%
# Import packages
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, time, date
import time

# Import csv
edinburgh_raw = pd.read_csv('./data/IEDINBUR6_weather.csv')
print(type(edinburgh_raw))


#%%
# View first few rows of the dataset
edinburgh_raw.head()

#%% [markdown]
# ## Extract temperature data
# 
# Rename the temp and date columns, then extract only those columns and save to a new data frame

#%%
# Rename temp and date column and convert temp to float, and date to datetime64
edinburgh_raw['temp'] = edinburgh_raw['TemperatureC'].astype(float)
edinburgh_raw['date'] = pd.to_datetime(edinburgh_raw['DateUTC'])


# Extract only date and temperature data
edinburgh_data = edinburgh_raw.loc[:,['date', 'temp']]


#%%
# View the segment of the data set we've selected
edinburgh_data.head()

#%% [markdown]
# ## Calculate daily averages
# 
# For rows that share the same date, calculate the average temp of each group. Create a new dataframe with average temp per day.

#%%
# Use .describe() to get an idea of what's in the dataset
edinburgh_data.describe()

# Strip time from date column
edinburgh_data['date'] = edinburgh_data['date'].apply(lambda edinburgh_data : 
datetime(year=edinburgh_data.year, month=edinburgh_data.month, day=edinburgh_data.day))

# Group by day, calculate mean of each day
edi_group = edinburgh_data.groupby('date').agg({'temp': 'mean'})

# Plot the grouped data
plt.plot(edi_group)
plt.show()

#%% [markdown]
# ## Removing outliers
# 
# The weather in Edinburgh shouldn't be getting below -20C ever...let's filter this dataset a bit
#%% [markdown]
# # Next steps
#  Clean up the dataset, convert tempC to tempF, plot vs time

