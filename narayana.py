import time


def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i == -1:
        arr.reverse()
        return False

    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1:] = reversed(arr[i + 1:])
    return True

lis = [1, 2, 3, 4, 5, 6, 7]
time_1 = time.time()
while next_permutation(lis):
    print(lis)
print(time.time() - time_1)
