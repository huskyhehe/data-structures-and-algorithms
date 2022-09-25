// https://leetcode.com/problems/remove-linked-list-elements

// linked list traversal + dummy head + two pointers
// Time: O(n)
// Space: O(1)

import model.ListNode;

public class Solution2 {
    public ListNode removeElements(ListNode head, int val) {

        if (head == null) return null;

        ListNode dummy = new ListNode(-1);
        dummy.next = head;

        ListNode pre = dummy;
        ListNode cur = head;
        while (cur != null) {
            if (cur.val == val) pre.next = cur.next;
            else pre = pre.next;
            cur = cur.next;
        }

        return dummy.next;
    }
}
