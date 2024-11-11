import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


def plot_temps(choice):
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and temperatures from this file.
        dates, temps = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            if choice.upper() == 'HIGH':
                temp = int(row[5])
                color = "red"
                label = 'High'
            if choice.upper() == 'LOW':
                temp = int(row[6])
                color = "blue"
                label = 'Low'
            temps.append(temp)


    # Plot the temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.plot(dates, temps, c=color)

    # Format plot.
    plt.title(f"Daily {label} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def main():
    print(f'Hello and welcome to WeatherService, where you can find the high temperatures and low temperatures from the airport in Sitka, Alaska.')
    print(f'Please indicate whether you want to view a chart on "low" temperatures or "high" temperatures by simply typing low or high. Type exit to stop.')


    while True:

        choice = input("> ")
        if choice.upper() not in ['HIGH', 'LOW', "EXIT"]:
            print(input('Invalid choice. Please try again.'))
        elif choice.upper() == 'EXIT':
            print('Thank you for using WeatherService. Goodbye!')
            sys.exit()
        else:
            plot_temps(choice)
            print("Select another option from the menu or type exit to quit.")


if __name__ == "__main__":
    main()
