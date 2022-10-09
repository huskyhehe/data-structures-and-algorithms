import heapq
from typing import List


# heap sort
# time: O(N * logK)
# space: O(K)
def find_kth_largest(nums: List[int], k: int) -> int:
    minheap = nums[:k]
    heapq.heapify(minheap)

    for i in range(k, len(nums)):
        if nums[i] > minheap[0]:
            heapq.heappop(minheap)
            heapq.heappush(minheap, nums[i])
    return minheap[0]


# def rotate_brute(nums: List[int], k: int) -> None:

# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

def rotate_reverse(nums: List[int], k: int) -> None:
    # corner case
    if len(nums) == 1 or k == 0:
        return

    n = len(nums)
    k %= n

    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


# Boyer Moore Voting Algorithm
def majority_element(nums: List[int]) -> int:
    candidate = nums[0]
    count = 1

    for num in nums[1:]:
        if num == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = num
                count = 1

    return candidate


if __name__ == "__main__":
    nums1 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k1 = 4
    print("kth largest: ")
    print(find_kth_largest(nums1, k1))

    nums2 = [1, 2, 3, 4, 5, 6, 7]
    k2 = 3
    rotate_reverse(nums2, 3)
    print("rotate:")
    print(nums2)

    nums3 = [2, 2, 1, 1, 1, 2, 2]
    print("majority element: ")
    print(majority_element(nums3))
