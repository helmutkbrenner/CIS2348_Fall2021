# Helmut Brenner #
# 2037275 #

if __name__ == '__main__':
    import math

    # Dictionary of paint colors and cost per gallon
    paint_colors = {
        'red': 35,
        'blue': 25,
        'green': 23
    }

    # FIXME (1): Prompt user to input wall's width
    # Calculate and output wall area
    wall_height = int(input('Enter wall height (feet):\n'))
    wall_width = int(input('Enter wall width (feet):\n'))
    wall_area = wall_width * wall_height
    print('Wall area: {} square feet'.format(wall_area))

    # FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
    print('Paint needed: {:.2f} gallons'.format(wall_area / 350))

    # FIXME (3): Calculate/output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
    print('Cans needed: {} can(s)\n'.format(math.ceil(wall_area / 350)))

    # FIXME (4): Calculate and output the total cost of paint can needed depending on color
    user_color = input('Choose a color to paint the wall:\n')
    print('Cost of purchasing {} paint: ${}'.format(user_color,  # this indentation pattern is pycharms doing.
                                                    paint_colors[user_color] * (math.ceil(wall_area / 350))))
