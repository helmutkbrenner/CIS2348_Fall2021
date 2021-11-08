#  Helmut Brenner  #
#  2037275  #

if __name__ == '__main__':
    #  take input as a list and turn it into the master list
    master_list = [int(x) for x in input().split()]

    #  use a comprehension to make a new list with only non-negative values
    unsorted_list = [i for i in master_list if i >= 0]
    sorted_list = sorted(unsorted_list)

    #  print values with spacing
    for i in range(len(sorted_list)):
        print(sorted_list[i], end=' ')
