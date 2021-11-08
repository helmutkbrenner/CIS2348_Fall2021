#  Helmut Brenner  #
#  2037275  #

if __name__ == '__main__':
    #  recycled code from the last problem but changed for strings.
    master_list = [str(x) for x in input().split()]
    my_dictionary = {}

    #  Loads the dictionary
    for i in master_list:
        if i not in my_dictionary:
            my_dictionary[i] = 1
        else:
            my_dictionary[i] += 1

    #  prints the words in order, with the number of times that word shows up in the whole string
    for j in master_list:
        print(j, my_dictionary[j])
