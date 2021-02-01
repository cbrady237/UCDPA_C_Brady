
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


#2.2 Import a CSV file into a Pandas DataFrame
file = 'dublinbikes_2020_Q3.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())

#Graph 9AM - 2020-07-01 09:05:02
df2 = df.set_index("TIME")
df2["PERCENT AVAILABLE"] = df2["AVAILABLE BIKES"] / df2["BIKE STANDS"]
hour_9 = df2.loc['2020-07-01 09:05:02']
print(hour_9.head())
stations = [37, 38, 113, 69]
hour9 = hour_9.set_index("STATION ID")
print(hour9.head())
hour_9am = hour9.loc[stations]
print(hour_9am)
hour_9am = hour_9am.set_index("LAST UPDATED")
print(hour_9am)

sns.set_theme(style="whitegrid")
ax = sns.barplot(x="NAME", y="AVAILABLE BIKES", data=hour_9am)
ax.set_title('Bikes available at 9am')
ax.set_xlabel('STATION')
plt.show()