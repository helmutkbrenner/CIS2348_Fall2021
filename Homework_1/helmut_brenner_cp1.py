# Helmut Brenner #
# 2037275 #

import datetime

if __name__ == '__main__':
    # Print Title
    print('Birthday Calculator')
    print('Current Day')

    # Get current Date from User
    current_month = int(input('Current Month: '))
    current_date = int(input('Current Day: '))
    current_year = int(input('Current Year: '))

    # Get user birthday
    print('Next, What is your birthday?')

    user_b_month = int(input('Birth Month:'))
    user_b_day = int(input('Birthday:'))
    user_b_year = int(input('Birth Year:'))

    # Here using the datetime module I load the user input into the provided classes and
    # then perform date math.
    current_day = datetime.date(current_year, current_month, current_date)
    user_birthday = datetime.date(user_b_year, user_b_month, user_b_day)

    time_delta = current_day - user_birthday
    years_old = time_delta.days//365

    # A simple if statement to check for the users birthday, else print the age in years with
    # a message.
    if current_date == user_b_day and current_month == user_b_month:
        print('Happy birthday, you are {} years old today!'.format(years_old))
    else:
        print('You are {} years old!'.format(years_old))
