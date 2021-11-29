#  Helmut Brenner  #
#  2037275  #

def selection_sort_descend_trace(integer_list):
    for k in range(len(integer_list) - 1):
        index_of_smallest = k
        for j in range(k + 1, len(integer_list)):
            if integer_list[j] > integer_list[index_of_smallest]:
                index_of_smallest = j

        number = integer_list[k]
        integer_list[k] = integer_list[index_of_smallest]
        integer_list[index_of_smallest] = number
        print(' '.join(integer_list) + ' ')


if __name__ == '__main__':
    number_list = input()
    list = number_list.split()
    selection_sort_descend_trace(list)
