# Helmut brenner #
# 2037275 #

if __name__ == '__main__':
    user_num1 = int(input('Enter integer:\n'))

    print('You entered: {}'.format(user_num1))

    print('{} squared is {}'.format(user_num1, (user_num1 * user_num1)))

    print('And {} cubed is {} !!'.format(user_num1, (user_num1 * user_num1 * user_num1)))

    user_num2 = int(input('Enter another integer:\n'))

    print('{} + {} is {}'.format(user_num1, user_num2, (user_num1 + user_num2)))

    print('{} * {} is {}'.format(user_num1, user_num2, (user_num1 * user_num2)))
