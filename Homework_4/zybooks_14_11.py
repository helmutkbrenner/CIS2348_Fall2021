#  Helmut Brenner  #
#  2037275  #

def selection_sort_descend_trace(string_list):
    #  Takes the string of integers and turns it into a list of int
    integer_list = [int(i) for i in string_list]
    for k in range(len(integer_list) - 1):
        index_of_smallest = k
        for j in range(k + 1, len(integer_list)):
            if integer_list[j] > integer_list[index_of_smallest]:
                index_of_smallest = j

        number = integer_list[k]
        integer_list[k] = integer_list[index_of_smallest]
        integer_list[index_of_smallest] = number

        #  Zybooks wants the output to be in string form again so a little reverse while loading string ints into a list
        formatted_numbers = ' '.join([str(i) for i in integer_list])
        print(formatted_numbers + ' ')


if __name__ == '__main__':
    number_list = input()
    list = number_list.split()
    selection_sort_descend_trace(list)
