// https://leetcode.com/problems/split-linked-list-in-parts/

// linked list traversal + two pointers
// Time: O(n + k)
// Space: O(max(n, k)

import model.ListNode;

public class Solution4 {
    public ListNode[] splitListToParts(ListNode head, int k) {
        int n = 0;
        ListNode temp = head;
        while (temp != null) {
            n ++;
            temp = temp.next;
        }

        int size = n / k;
        int largerSizeCount = n % k;

        ListNode[] res = new ListNode[k];
        ListNode pre = null;
        ListNode cur = head;

        for (int i = 0; i < k; i ++) {
            res[i] = cur;
            int larger = i < largerSizeCount? 1: 0;

            for (int j = 0; j < size + larger; j ++) {
                pre = cur;
                cur = cur.next;
            }

            if (pre != null) {
                pre.next = null;
            }
        }

        return res;
    }
}
