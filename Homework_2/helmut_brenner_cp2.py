# Helmut Brenner # 
# 2037275 #

import datetime

if __name__ == '__main__':
    months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    # This block opens the file inputDates.txt and reads all the lines into a list of strings
    file = open('inputDates.txt')
    line_list = file.readlines()
    file.close()

    # these next statements check for incorrect date formats. I understand this is probably not the best way so
    # I will continue to think about iterative improvements.
    middle_list = []
    for i in range(len(line_list)):
        if line_list[i].count(' ') == 2 and line_list[i].count(',') == 1 and line_list[i].find('.') == -1:
            middle_list.append(line_list[i])
    print(line_list)

    # This next block of code will parse the dates into variables which can then be compared to the current date.
    final_list = []
    for i in range(len(middle_list)):
        temp_year = int(middle_list[i][-5:])

        temp_month = middle_list[i][:middle_list[i].find(' ')]
        temp_month_int = int(months_list.index(temp_month)+1)

        temp_day = int(middle_list[i][middle_list[i].find(' '):middle_list[i].find(',')])

        # This is where I use the datetime module to load up the parsed dates into an date object for easy formatting
        # and comparison.

        date_constructed = datetime.datetime(temp_year, temp_month_int, temp_day)
        current_date = datetime.datetime.now()

        if date_constructed <= current_date:
            formatted_string = date_constructed.strftime("%#m/%#d/%Y")
            final_list.append(formatted_string)

        print(temp_year, ',', temp_month, ',', temp_month_int, ',', temp_day)

    for i in range(len(final_list)):
        print(final_list[i])
