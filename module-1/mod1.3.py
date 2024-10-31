'''
Anton DeCesare mod 1.3
This programs takes an input of number of beers and counts them off the wall!

'''


# Function to handle number of beers and counts down
def countdown(number_of_beers):
    # Beers gone, loop over
    if number_of_beers == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    else:
        # Print beer singular
        if number_of_beers == 1:
            print(f"{number_of_beers} bottle of beer on the wall, {number_of_beers} bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        else:
        #Print number of beers
            print(f"{number_of_beers} bottles of beer on the wall, {number_of_beers} bottles of beer.")
            print(f"Take one down and pass it around, {number_of_beers - 1} bottles of beer on the wall.\n")
        # Recursively count down number of beers
        countdown(number_of_beers - 1)


def main():
    # Initiate number of beers to start at
    number_of_beers = int(input("Enter the number of beers: "))
    if number_of_beers <= 0:
        print("Invalid input. Please enter a positive integer.")
        return

    print("Starting the song with", number_of_beers, "bottles of beer on the wall...\n")
    countdown(number_of_beers)


if __name__ == "__main__":
    main()
