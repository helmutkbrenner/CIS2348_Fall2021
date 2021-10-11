# Helmut Brenner #
# 2037275 #

def palindrome_checker(word):
    #  This function takes the string characters and loads them into a list, splice/reverses them and compares.
    #  It then returns a boolean indicator.
    char_list = []
    palindrome = False
    for i in range(len(word)):
        if word[i] != ' ':
            char_list.append(word[i])

    rev_char_list = char_list[::-1]

    if rev_char_list == char_list:
        palindrome = True

    return palindrome


if __name__ == '__main__':
    #  main function calls the function and prints the statement
    user_word = str(input())
    if palindrome_checker(user_word):
        print('{} is a palindrome'.format(user_word))
    else:
        print('{} is not a palindrome'.format(user_word))
