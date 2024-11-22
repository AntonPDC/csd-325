import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = 'W'

# Settings for simulation probabilities:
INITIAL_TREE_DENSITY = 0.50  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.
PAUSE_LENGTH = 0.5  # Time to pause between simulation steps.


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main simulation loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue

                # Rules for each cell in the forest:
                if forest[(x, y)] == EMPTY and random.random() <= GROW_CHANCE:
                    nextForest[(x, y)] = TREE
                elif forest[(x, y)] == TREE and random.random() <= FIRE_CHANCE:
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # Spread fire to neighboring trees, skipping water cells:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = (x + ix, y + iy)
                            if forest.get(neighbor) == TREE:
                                nextForest[neighbor] = FIRE
                    nextForest[(x, y)] = EMPTY
                else:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure, including a lake."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    # Define lake parameters:
    lake_start_x, lake_start_y = 30, 10  # Top-left corner of the lake.
    lake_width, lake_height = 20, 5      # Dimensions of the lake.

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Create the lake area:
            if lake_start_x <= x < lake_start_x + lake_width and lake_start_y <= y < lake_start_y + lake_height:
                forest[(x, y)] = WATER
            elif random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Reset to default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
