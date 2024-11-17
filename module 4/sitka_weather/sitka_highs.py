import csv
from datetime import datetime

from matplotlib import pyplot as plt

print(f'Hello and welcome to WeatherService, where you can find the high temperatures and low temperatures from the airport in Sitka, Alaska.')
print(f'Please indicate whether you want to view a chart on "low" temperatures or "high" temperatures by simply typing low or high. Type exit to stop.')
choice = input().upper()
if choice != 'HIGH' or choice != 'LOW' or choice != 'EXIT':
    print(input('Invalid choice. Please try again.'))
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)


# Plot the high temperatures.
#plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
