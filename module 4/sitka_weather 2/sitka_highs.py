import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

# Display menu instructions
print("Welcome to the Sitka Weather Program!")
print("Select an option from the menu:")
print("1. Highs")
print("2. Lows")
print("3. Exit")

# Main loop
while True:
    choice = input("Enter your choice (1 for Highs, 2 for Lows, 3 to Exit): ")
    if choice == '3':
        print("Thank you for using the Sitka Weather Program. Goodbye!")
        sys.exit()
    elif choice not in ['1', '2']:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and temperatures from this file.
        dates, temps = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            if choice == '1':
                temp = int(row[5])  # High temperatures
            elif choice == '2':
                temp = int(row[6])  # Low temperatures
            temps.append(temp)

    # Plot the selected temperatures.
    fig, ax = plt.subplots()
    color = 'red' if choice == '1' else 'blue'
    label = "High" if choice == '1' else "Low"
    ax.plot(dates, temps, c=color)

    # Format plot.
    plt.title(f"Daily {label} Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # Show the plot
    plt.show()

    print("Select another option from the menu or choose 3 to exit.")
