# Helmut Brenner #
# 2037275 #

if __name__ == '__main__':
    #  First thing, get user input. Decided to use floats on everything for decimal accuracy.

    cupslemjuice = float(input('Enter the amount of lemon juice (in cups):\n'))
    cupswater = float(input('Enter amount of water (in cups):\n'))
    cupsagave = float(input('Enter amount of agave nectar (in cups):\n'))
    numservings = float(input('How many servings does this make?\n'))

    #  Output the ingredient list to the screen

    print('Lemonade Ingredients - yields {:.2f} servings'.format(numservings))
    print('{:.2f} cup(s) lemon juice'.format(cupslemjuice))
    print('{:.2f} cup(s) water'.format(cupswater))
    print('{:.2f} cup(s) agave nectar'.format(cupsagave))

    # Get desired number of servings

    desiredservings = int(input('How many servings would you like to make?\n'))

