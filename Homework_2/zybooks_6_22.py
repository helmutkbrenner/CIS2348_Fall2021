# Helmut Brenner #
# 2037275 #

if __name__ == '__main__':
    int_A1 = int(input())
    int_B1 = int(input())
    int_C1 = int(input())

    int_A2 = int(input())
    int_B2 = int(input())
    int_C2 = int(input())

    for x in range(-10, 11):
        for y in range(-10, 11):
            if (int_A1*x) + (int_B2*y) == int_C1 and (int_A2*x) - (int_B2*y) == int_C2:
                print(x, ' ', y)
    print('No solution')
