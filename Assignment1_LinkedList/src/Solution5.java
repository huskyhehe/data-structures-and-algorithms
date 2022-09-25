// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

import model.ListNode;

public class Solution5 {
    public ListNode insert(ListNode head, int insertVal) {

        ListNode newNode = new ListNode(insertVal);

        if (head == null) {
            newNode.next = newNode;
            return newNode;
        }

        if (head.next == null) {
            head.next = newNode;
            newNode.next = head;
            return head;
        }

        ListNode pre = head;
        ListNode cur = head.next;

        while (cur != head) {
            if (pre.val <= insertVal && insertVal <= cur.val) break;
            if (pre.val > cur.val) {
                if (insertVal > pre.val || insertVal < cur.val) break;
            }
            pre = pre.next;
            cur = cur.next;
        }
        pre.next = newNode;
        newNode.next = cur;

        return head;
    }
}
