# find the minimum and move it to the front
# time: O(n²)
# space: O(1)
# not stable

from typing import List


def selection_sort(arr: List[int]):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9]
    selection_sort(data)
    print(data)
