import heapq
from typing import List


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


if __name__ == "__main__":
    nums1 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k1 = 4
    print(find_kth_largest(nums1, k1))
