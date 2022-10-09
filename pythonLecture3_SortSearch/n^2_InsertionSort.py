# Compare cur with each element on the left until an element smaller than it is found
# time: O(n²)
# space: O(1)
# stable

from typing import List


def insertion_sort(arr: List[int]):
    for i in range(1, len(arr)):
        j = i
        while j - 1 >= 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


def insertion_sort_optimized(arr: List[int]):
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i - 1
        while j >= 0 and cur < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur


if __name__ == '__main__':
    data1 = [-2, 45, 0, 11, -9]
    insertion_sort(data1)
    print(data1)

    data2 = [-2, 45, 0, 11, -9]
    insertion_sort_optimized(data2)
    print(data2)
