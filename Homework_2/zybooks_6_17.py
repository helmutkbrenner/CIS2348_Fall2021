# Helmut Brenner #
# 2037275 #

if __name__ == '__main__':
    # Made a dictionary with key value pairs
    cipher = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}
    appendix = 'q*s'

    user_pass = str(input())
    strong_pass = ''
    # constructs a new string while referencing the dictionary.
    for i in range(len(user_pass)):
        if user_pass[i] in cipher:
            strong_pass += cipher[user_pass[i]]
        else:
            strong_pass += user_pass[i]
    strong_pass += appendix
    print(strong_pass)
