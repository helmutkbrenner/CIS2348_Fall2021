# Helmut Brenner #
# 2037275 #

import csv

if __name__ == '__main__':
    word_counts = {}
    with open('input1.csv', 'r') as input1:
        data_line = csv.reader(input1, delimiter=',')
        for row in data_line:
            for word in row:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1

    print(word_counts)
