# Helmut Brenner #
# 2037275 #

import datetime

if __name__ == '__main__':
    print('Birthday Calculator')
    print('Current Day')

    current_month = int(input('Current Month: '))
    current_date = int(input('Current Day: '))
    current_year = int(input('Current Year: '))

    print('Next, What is your birthday?')

    user_b_month = int(input('Birth Month:'))
    user_b_day = int(input('Birthday:'))
    user_b_year = int(input('Birth Year:'))

    current_day = datetime.date(current_year, current_month, current_date)
    user_birthday = datetime.date(user_b_year, user_b_month, user_b_day)

    time_delta = current_day - user_birthday
    years_old = time_delta.days//365

    if current_date == user_b_day & current_month == user_b_month:
        print('Happy birthday, you are {} years old.'.format(years_old))
    else:
        print('You are {} years old!'.format(years_old))








