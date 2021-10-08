# Helmut Brenner # 
# 2037275 #

import datetime

if __name__ == '__main__':
    # this block takes user input line by line and loads it into a list of strings.
    line_list = []
    user_line_input = ''
    while user_line_input != '-1':
        user_line_input = input()
        line_list.append(user_line_input)
    print(line_list)