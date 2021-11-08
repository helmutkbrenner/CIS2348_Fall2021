#  Helmut Brenner  #
#  2037275  #

if __name__ == '__main__':
    master_list = input()
    answer_list = []
    for i in range(len(master_list)):
        if master_list[i] > 0:
            if master_list[i] >= answer_list[-1]:
                answer_list.append(master_list[i])
    print(answer_list)
