# compare adjacent and swap
# time: O(n²)
# space: O(1)
# stable

from typing import List


def bubble_sort(arr: List[int]):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_optimized(arr: List[int]):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    data1 = [-2, 45, 0, 11, -9]
    bubble_sort(data1)
    print(data1)

    data2 = [-2, 45, 0, 11, -9]
    bubble_sort_optimized(data2)
    print(data2)
