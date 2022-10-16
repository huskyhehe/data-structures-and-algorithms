from typing import List


class Solution1:
    def rotate_array(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(arr: List[int], start: int, end: int) -> None:
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)




