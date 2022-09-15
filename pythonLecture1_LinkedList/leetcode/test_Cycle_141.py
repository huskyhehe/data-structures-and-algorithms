from unittest import TestCase

from leetcode.Cycle_141 import Solution
from leetcode.ListNode import ListNode


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()


class TestHasCycle(TestSolution):
    def test_case_pos1(self):
        # [3,2,0,-4] pos=1
        head = ListNode(3)
        cycle_pos = ListNode(2)
        head.next = cycle_pos
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(-4)
        head.next.next.next.next = cycle_pos
        self.assertEqual(self.solution.hasCycle(head), True)

    def test_case_pos0(self):
        # [1,2] pos=0
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = head
        self.assertEqual(self.solution.hasCycle(head), True)

    def test_case_no_cycle(self):
        # [1] pos=-1
        head = ListNode(1)
        self.assertEqual(self.solution.hasCycle(head), False)
