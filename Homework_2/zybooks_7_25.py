# Helmut Brenner #
# 2037275 #

def exact_change(number):
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = 0, 0, 0, 0, 0
    running_total = number

    while running_total >= 1.00:
        running_total -= 1.00
        num_dollars += 1
    print(running_total)
    while running_total >= .25:
        running_total -= .25
        num_quarters += 1
    print(running_total)
    while running_total >= .10:
        running_total -= .10
        num_dimes += 1
    print(running_total)
    while running_total >= .05:
        running_total -= .05
        num_nickels += 1
    print(running_total)
    while running_total >= .01:
        running_total -= .01
        num_pennies += 1
    print(running_total)
    print(num_dollars, num_quarters, num_dimes, num_nickels, num_pennies+1)
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies+1


if __name__ == '__main__':
    user_input = float(input())
    exact_change(user_input)
