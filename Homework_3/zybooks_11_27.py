#  Helmut Brenner  #
#  2037275  #

if __name__ == '__main__':
    my_dictionary = {}
    key_list = []

    for i in range(1, 6):
        print('Enter player {}\'s jersey number:'.format(i))
        jersey_number = int(input())
        print('Enter player {}\'s rating:')
        player_rating = int(input())
        my_dictionary[jersey_number] = player_rating
        key_list.append(jersey_number)

    for i in my_dictionary:
        print(i, my_dictionary[i])



