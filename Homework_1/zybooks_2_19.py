# Helmut Brenner #
# 2037275 #

if __name__ == '__main__':
    #  First thing, get user input. Decided to use floats on everything for decimal accuracy.

    cupslemjuice = float(input('Enter amount of lemon juice (in cups):\n'))
    cupswater = float(input('Enter amount of water (in cups):\n'))
    cupsagave = float(input('Enter amount of agave nectar (in cups):\n'))
    numservings = float(input('How many servings does this make?\n'))

    #  Output the ingredient list to the screen

    print('\nLemonade ingredients - yields {:.2f} servings'.format(numservings))
    print('{:.2f} cup(s) lemon juice'.format(cupslemjuice))
    print('{:.2f} cup(s) water'.format(cupswater))
    print('{:.2f} cup(s) agave nectar'.format(cupsagave))

    # Get desired number of servings

    desiredservings = int(input('How many servings would you like to make?\n'))

    # divide desired servings by num of servings in recipe to get multiplier for ingredients.

    mulitplier = desiredservings / numservings

    # reprint the ingredients list with the num of desired servings and adjusted ingredients list

    print('\nLemonade ingredients - yields {:.2f} servings'.format(desiredservings))
    print('{:.2f} cup(s) lemon juice'.format(cupslemjuice * mulitplier))
    print('{:.2f} cup(s) water'.format(cupswater * mulitplier))
    print('{:.2f} cup(s) agave nectar'.format(cupsagave * mulitplier))

    # reprint the augmented ingredients list in gallon units.

    print('\nLemonade ingredients - yields {:.2f} servings'.format(desiredservings))
    print('{:.2f} gallon(s) lemon juice'.format((cupslemjuice * mulitplier)/16))
    print('{:.2f} gallon(s) water'.format((cupswater * mulitplier)/16))
    print('{:.2f} gallon(s) agave nectar'.format((cupsagave * mulitplier)/16))
