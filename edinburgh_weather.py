""" Import weather data from Edinburgh """

# Analyze average temp over a year
# Scatter plot of all weather data, then also plot the average
# Plot precipitation as well

# This project is to get used to Python syntax for importing data
# Pandas should be similar to R so this is also a refresher


#%%
# Step 0: Get pandas
import pandas as pd

# Step 1: Find working directory
import os
print(os.getcwd())

# Step 2: Import csv

data = pd.read_csv('./data/IEDINBUR6_weather.csv')
print(type(data))

#%%
# View first few rows of the dataset
data.head()

#%% [markdown]

## Next steps

# Clean up the dataset, convert tempC to tempF, plot vs time