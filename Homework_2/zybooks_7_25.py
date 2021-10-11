# Helmut Brenner #
# 2037275 #

def exact_change(number):
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = 0, 0, 0, 0, 0
    running_total = number

    while running_total >= 100:
        running_total -= 100
        num_dollars += 1
    while running_total >= 25:
        running_total -= 25
        num_quarters += 1
    while running_total >= 10:
        running_total -= 10
        num_dimes += 1
    while running_total >= 5:
        running_total -= 5
        num_nickels += 1
    while running_total >= 1:
        running_total -= 1
        num_pennies += 1
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies+1


if __name__ == '__main__':
    user_input = float(input())
    if user_input <= 0:
        print('no change')
    exact_change(user_input)
