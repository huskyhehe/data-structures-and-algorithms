// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

// linked list traversal
// Time: O(n)
// Space: O(1)

import model.ListNode;

public class Solution3 {
    public ListNode swapNodes(ListNode head, int k) {

        int n = 0;
        ListNode cur = head;
        while (cur != null) {
            n ++;
            cur = cur.next;
        }

        ListNode beginKth = head;
        ListNode endKth = head;
        for (int i = 1; i < k; i ++) beginKth = beginKth.next;
        for (int i = 1; i < n - k + 1; i ++) endKth = endKth.next;

        swapVals(beginKth, endKth);
        return head;
    }

    public void swapVals(ListNode node1, ListNode node2) {
        int temp = node1.val;
        node1.val = node2.val;
        node2.val = temp;
    }
}
