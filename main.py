#Importing data
#2.1 Import API

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

# Import pandas as pd
import pandas as pd

file = 'dublinbikes_2020_Q3.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())

#second file
file2 = 'dublin.csv'
dublin_bikes = pd.read_csv(file2)
print(dublin_bikes.head())
dublin_bikes_ind = dublin_bikes.set_index(["NAME"])
print(dublin_bikes_ind.head())

#Convert Time column to datetime type
print(df['TIME'].dtypes)
df['TIME'] =  pd.to_datetime(df['TIME'])
print(df['TIME'].dtypes)

#Add weekday column using time
df["weekday"] = df['TIME'].dt. day_name()
print(df.head())

#Analyzing data
#1. Your project should include sorting, indexing, grouping.
df_station = df.groupby('NAME')

print(df_station.first())

#Extract Name and number of bike stands for summary




#Drop duplicates from index
bike_stands = df.drop_duplicates(subset=["NAME", "BIKE STANDS"])
print(bike_stands.head())
bike_stands.to_csv('bike_stands.csv',index = False)

#Index
bike_stands_ind = bike_stands.set_index(["NAME", "BIKE STANDS"])
print(bike_stands_ind.head())


#Extract Weekdays from df using loc
print(df['weekday'].dtypes)
df_weekday = df.set_index("weekday")

#Create list
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(df_weekday.loc[weekdays])

# for loop / iterrows
print(df['BIKE STANDS'].dtypes)

for key, row in bike_stands_ind.head().iterrows():
    print(key)
    print(row)


#Merge dataframes
dublin_bikes_summary = dublin_bikes_ind.merge(bike_stands[["NAME", "BIKE STANDS"]], on = "NAME", how = 'left')

print(dublin_bikes_summary.head())
dublin_bikes_summary.to_csv('dublin_bikes_summary.csv',index = False)

#dublin_bikes_summary.plot(x = 'Name', y = 'BIKE STANDS', kind = ' scatter')
#plt.show()

date = ['2020-07-01 08:30:02']
df_date = df.set_index("TIME")
df_July1 = df_date.loc[date]
print(df_July1.head())

July0120 = df_July1.to_numpy()
print(July0120)

np_July = np.array(July0120)

#On July 1 2020, % of available bikes using numpys
np_total_bikes = np_July[:,3]
print(np_total_bikes)
np_available_bikes = np_July[:,5]
print(np_available_bikes)
np_percentage_available_bikes = np_available_bikes / np_total_bikes
print(np_percentage_available_bikes)



# Add columns with year, month, and weekday name
df_date['Year'] = df_date.index.year
df_date['Month'] = df_date.index.month
df_date['Hour'] = df_date.index.hour
print(df_date.head(30))
# Display a random sampling of 5 rows



hour = df_date.set_index("Hour")
hour["PERCENT AVAILABLE"] = hour["AVAILABLE BIKES"] / hour["BIKE STANDS"]
print(hour.head(25))
AM = [7, 8, 9, 10]
hour_AM = hour.loc[AM]
hour_AM2 = hour_AM[["NAME", "BIKE STANDS", "AVAILABLE BIKES"]]
hour_AM2["PERCENT AVAILABLE"] = hour_AM2["AVAILABLE BIKES"] / hour_AM2["BIKE STANDS"]
print(hour_AM.head(10))
print(hour_AM2.head(10))

#sns.pairplot(x="AVAILABLE BIKES", y="BIKE STANDS",
 #               data = hour_AM,
  #              kind = "scatter")

sns.set(rc={'figure.figsize':(11, 4)})
sns.relplot(x="TIME", y="PERCENT AVAILABLE",
            data=hour,
            kind="scatter")
#hour['PERCENT AVAILABLE'].plot(linewidth=2)
plt.show()

#ax = hour.loc['', 'PERCENT AVAILABLE'].plot()
#ax.set_ylabel('Percent Available');
#plt.show()

#g = sns.pairplot(hour_AM, vars=["HOUR", "AVAILABLE BIKES"])
#plt.show()

#Charts
#sns.relplot(x="NAME", y=["AVAILABLE BIKES" < 20],
#            data=df_July1,
 #           kind="scatter", col='NAME')

# Show plot
#plt.show()


#x = np_total_bikes
#y = np_available_bikes
#sns.pairplot(df_July1, hue="BIKE STANDS")

# Display the plot
#plt.show()





