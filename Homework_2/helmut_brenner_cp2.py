# Helmut Brenner # 
# 2037275 #

import datetime

if __name__ == '__main__':
    months_list = ['January','February','March','April','May','June','July','August','September','October',
                   'November','December']
    # this block takes user input line by line and loads it into a list of strings.
    line_list = []
    user_line_input = ''
    while user_line_input != '-1':
        user_line_input = str(input())
        # these next statements check for incorrect date formats. I understand this is probably not the best way so
        # I will continue to think about iterative improvements.
        if user_line_input.count(' ') == 2 and user_line_input.count(',') == 1 and user_line_input.find('.') == -1:
            line_list.append(user_line_input)
    print(line_list)
    # This next block of code will parse the dates ito a datetime object
