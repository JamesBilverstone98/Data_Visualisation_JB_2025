from pathlib import Path
import csv # Python's csv module parses the lines in a csv file
from datetime import datetime # imports datetime class from the datetime module

import matplotlib.pyplot as plt


# the csv module we want to import and the file we want to work with
path = Path('weather_data/sitka_weather_2021_simple.csv') 
lines = path.read_text().splitlines()

reader = csv.reader(lines) # this is an object that can be used to parse lines
header_row = next(reader) # returns the next line in the file - the headers

# Extract dates and high/low temperatures
dates, highs, lows = [], [], [] 
for row in reader: 
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
    
# plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# alpha argument controls a colours transparency 
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
# fill between method for shading between the x and y values
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# format the plot
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # draws date labels diagonally to stop overlapping
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

