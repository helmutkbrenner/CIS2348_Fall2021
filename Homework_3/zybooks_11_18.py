#  Helmut Brenner  #
#  2037275  #

if __name__ == '__main__':
    master_list = [int(x) for x in input().split()]

    unsorted_list = [i for i in master_list if i >= 0]
    sorted_list = sorted(unsorted_list)

    for i in range(len(sorted_list)):
        print(sorted_list[i], end=' ')
