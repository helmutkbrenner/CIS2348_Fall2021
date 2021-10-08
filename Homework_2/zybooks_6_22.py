# Helmut Brenner #
# 2037275 #

if __name__ == '__main__':
    int_A1 = int(input())
    int_B1 = int(input())
    int_C1 = int(input())

    int_A2 = int(input())
    int_B2 = int(input())
    int_C2 = int(input())
    has_answer = False

    for x in range(-10, 11):
        for y in range(-10, 11):
            answer1 = (int_A1 * x) + (int_B1 * y)
            answer2 = (int_A2 * x) + (int_B2 * y)
            if answer1 == int_C1 and answer2 == int_C2:
                print(x, y)
                has_answer = True
    if not has_answer:
        print('No solution')
