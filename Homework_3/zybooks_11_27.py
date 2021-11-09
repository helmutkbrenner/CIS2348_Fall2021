#  Helmut Brenner  #
#  2037275  #

def print_menu():
    #  Prints the main menu
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')


if __name__ == '__main__':
    my_dictionary = {}
    key_list = []

    for i in range(1, 6):
        print('Enter player {}\'s jersey number:'.format(i))
        jersey_number = int(input())
        print('Enter player {}\'s rating:\n'.format(i))
        player_rating = int(input())
        my_dictionary[jersey_number] = player_rating
        key_list.append([jersey_number, player_rating])

    from operator import itemgetter
    sorted_key_list = sorted(key_list, key=itemgetter(0))

    print('ROSTER')
    for i in range(len(sorted_key_list)):
        j_number = sorted_key_list[i][0]
        print('Jersey number: {}, Rating: {}'.format(j_number, my_dictionary[j_number]))

    print_menu()
    user_command = ''
    while user_command != 'q':
        user_command = str(input('\nChoose an option:\n'))
        if user_command == 'a':
            #  Add Player
            print('Enter a new player\'s jersey number:')
            new_jersey_num = int(input())
            print('Enter the player\'s rating:')
            new_player_rating = int(input())

            #  add the inputs to dictionary and a list
            my_dictionary[new_jersey_num] = new_player_rating
            key_list.append([new_jersey_num, new_player_rating])

            #  Resort and assign the sorted key list
            from operator import itemgetter
            sorted_key_list = sorted(key_list, key=itemgetter(0))

            print_menu()
            continue
        elif user_command == 'd':
            #  Remove Player
            print('Enter a jersey number:')
            player_to_remove = int(input())
            del my_dictionary[player_to_remove]
            sorted_key_list.remove([player_to_remove, my_dictionary[player_to_remove]])
            print_menu()
            continue
        elif user_command == 'u':
            #  Update Player rating
            print('Enter a jersey number:')
            player_to_update = int(input())
            print('Enter a new rating for player:')
            updated_rating = int(input())
            my_dictionary[player_to_update] = updated_rating
            print_menu()
            continue
        elif user_command == 'r':
            #  Output players above a rating
            print('Enter a rating:')
            thresh_hold = int(input())
            above_x_list = []

            #  Test for being above the thresh hold
            for player_number, rating in my_dictionary.items():
                if rating > thresh_hold:
                    above_x_list.append([player_number, rating])

            #  sort qualifying entries by jersey number, ascending
            sorted_above_x_list = sorted(above_x_list, key=itemgetter(0))

            print('\nABOVE {}'.format(thresh_hold))
            for i in range(len(sorted_above_x_list)):
                j1_number = sorted_above_x_list[i][0]
                print('Jersey number: {}, Rating: {}'.format(j1_number, my_dictionary[j1_number]))
            print_menu()
            continue
        elif user_command == 'o':
            #  Output a roster
            print('\nROSTER')
            for i in range(len(sorted_key_list)):
                j_number = sorted_key_list[i][0]
                print('Jersey number: {}, Rating: {}'.format(j_number, my_dictionary[j_number]))
            print_menu()
            continue
        else:
            continue
