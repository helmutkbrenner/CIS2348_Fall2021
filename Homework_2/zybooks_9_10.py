# Helmut Brenner #
# 2037275 #

import csv

if __name__ == '__main__':
    user_input = str(input())
    word_counts = {}
    #  Used a with statement to ensure file close. Then iterate through the row and words in the data_line.
    #  then an if statement increments values or adds a key.
    with open(user_input, 'r') as input1:
        data_line = csv.reader(input1, delimiter=',')
        for row in data_line:
            for word in row:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1

    #  prints the dictionary with formatting
    for key in word_counts:
        print('{} {}'.format(key, word_counts[key]))
