
#Importing data from main file to run graph

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


# Import a CSV file into a Pandas DataFrame
file = 'dublinbikes_2020_Q3.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())


#Graph - 5PM - 2020-07-01 17:30:02
df2 = df.set_index("TIME")
df2["PERCENT AVAILABLE"] = df2["AVAILABLE BIKES"] / df2["BIKE STANDS"]
hour_5 = df2.loc['2020-07-01 17:30:02']
print(hour_5.head())
stations = [37, 38, 113, 69]
hour5 = hour_5.set_index("STATION ID")
print(hour5.head())
hour_5pm = hour5.loc[stations]
print(hour_5pm)
hour_5pm = hour_5pm.set_index("LAST UPDATED")
print(hour_5pm)

sns.set_theme(style="whitegrid")
ax = sns.barplot(x="NAME", y="AVAILABLE BIKES", data=hour_5pm)
ax.set_title('Bikes available at 5:30pm')
ax.set_xlabel('STATION')
plt.show()