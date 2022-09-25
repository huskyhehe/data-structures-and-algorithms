//https://leetcode.com/problems/rotate-list/

// linked list traversal
// Time: O(n)
// Space: O(1)

import model.ListNode;

public class Solution1 {
    public ListNode rotateRight(ListNode head, int k) {

        if (head == null || head.next == null) return head;

        int n = 1;
        ListNode tail = head;
        while (tail.next != null) {
            n ++;
            tail = tail.next;
        }
        tail.next = head;

        ListNode newTail = head;
        for (int i = 0; i < n - k % n - 1; i ++) {
            newTail = newTail.next;
        }
        ListNode newHead = newTail.next;
        newTail.next = null;

        return newHead;
    }
}
