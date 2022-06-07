"""Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

"""

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def pull_to_front(arr, start, end, letter):
    i = start
    j = end
    last_index = -1

    while i < j:
        if arr[i] == letter:
            last_index = i
            i += 1
        elif arr[j] != letter:
            j -= 1
        else:
            last_index = i
            swap(arr, i, j)

    return last_index


def reorder(arr):
    last_index = pull_to_front(arr, 0, len(arr) - 1, "R")
    pull_to_front(arr, last_index + 1, len(arr) - 1, "G")

    return arr

print(reorder(['G', 'B', 'R', 'R', 'B', 'R', 'G']))


