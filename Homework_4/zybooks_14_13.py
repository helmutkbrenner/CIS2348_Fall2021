#  Helmut Brenner  #
#  2037275  #

# Global variable
num_calls = 0


def partition(user_ids, i, k):
    #  determine pivot value
    median = i + (k - i) // 2
    pivot_value = user_ids[median]

    #  assign low and high index
    l = i
    h = k
    finished = False

    # compare to pivot value and then increment if required
    while not finished:
        while user_ids[l] < pivot_value:
            l += 1
        while pivot_value < user_ids[h]:
            h -= 1
        if l >= h:
            finished = True
        else:
            #  swap numbers when h is to the left of l
            tmp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = tmp
            l += 1
            h -= 1
    return h


def quicksort(user_ids, i, k):
    #  allows for incrementing the global variable within the function
    global num_calls
    num_calls += 1
    if i >= k:
        return

    j = partition(user_ids, i, k)

    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)

    return


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
