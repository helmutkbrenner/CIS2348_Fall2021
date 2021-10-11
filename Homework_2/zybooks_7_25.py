# Helmut Brenner #
# 2037275 #

def exact_change(number):
    #  This function uses the modulo operator to find the max number of coins given a total
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
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


def print_nums(number_1, number_2, number_3, number_4, number_5):
    #  This function prints the number of coins and accounts for zero and plural situations
    if number_1 > 1:
        print('{} dollars'.format(number_1))
    elif number_1 == 1:
        print('{} dollar'.format(number_1))
    if number_2 > 1:
        print('{} quarters'.format(number_2))
    elif number_2 == 1:
        print('{} quarter'.format(number_2))
    if number_3 > 1:
        print('{} dimes'.format(number_3))
    elif number_3 == 1:
        print('{} dime'.format(number_3))
    if number_4 > 1:
        print('{} nickels'.format(number_4))
    elif number_4 == 1:
        print('{} nickel'.format(number_4))
    if number_5 > 1:
        print('{} pennies'.format(number_5))
    elif number_5 == 1:
        print('{} penny'.format(number_5))
    return 0


#  This is the main function which gets input and then uses the functions to calculate and display the information
if __name__ == '__main__':
    user_input = float(input())
    if user_input <= 0:
        print('no change')
    coin_list = exact_change(user_input)
    print_nums(coin_list[0], coin_list[1], coin_list[2], coin_list[3], coin_list[4])
