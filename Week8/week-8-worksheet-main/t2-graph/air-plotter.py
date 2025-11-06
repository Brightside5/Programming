'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''
import pandas as pd
import matplotlib.pyplot as plt

#define the filename and columns
filename = "leeds-centre-air-quality.csv"
pollution_columns = [
    " pm25",
    " pm10",
    " o3",
    " no2"
]
date_column = "date"

#read the data
data = pd.read_csv(filename)
#get the average pollution data
data["average_pollution"]=data[pollution_columns].mean(axis=1)

#transform the format of date
data[date_column] = pd.to_datetime(data[date_column], format='%d/%m/%Y')
#sort by date to draw a graph
data = data.sort_values(by=date_column)

#set the size and constants of the graph
plt.figure(figsize=(12,6))
plt.plot(data[date_column],data['average_pollution'], marker='o', markersize=2, linestyle='-')
#set the title and name of axises
plt.title("Leeds Central Average Air Pollution (Hangming Hu)")
plt.xlabel("date")
plt.ylabel("average pollution")
plt.grid(True) #show the grid
plt.show()