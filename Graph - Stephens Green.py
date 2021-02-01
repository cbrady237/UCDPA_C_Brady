#Preparing data for graph as per main py file

# Import requests package
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Assign URL to variable: url
url = 'https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=4aed48738d7bb38f74643c9e926692a1c6501a45'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Print the text of the response
print(r.text)
# Decode the JSON data into a dictionary: json_data
json_data = r.json()



#2.2 Import a CSV file into a Pandas DataFrame
file = 'dublinbikes_2020_Q3.csv'


# Read the file into a DataFrame: df
df = pd.read_csv(file)
df['TIME'] =  pd.to_datetime(df['TIME'])
df_date = df.set_index("TIME")
df_date['Year'] = df_date.index.year
df_date['Month'] = df_date.index.month
df_date['Hour'] = df_date.index.hour
hour = df_date.set_index("Hour")
hour["PERCENT AVAILABLE"] = hour["AVAILABLE BIKES"] / hour["BIKE STANDS"]
print(hour.head())

hour = df_date.set_index("NAME")
hour_SG = hour.loc["ST. STEPHEN'S GREEN SOUTH"]
print(hour_SG.head())

#Graph - Stephens Green South 010720
fig, ax = plt.subplots()
ax.plot(hour_SG['LAST UPDATED'], hour_SG['AVAILABLE BIKES'])
ax.set_title('ST. STEPHENS GREEN SOUTH - 01/07/20')
ax.set_xlabel('Time')
ax.set_ylabel('Number of bikes available')
plt.show()