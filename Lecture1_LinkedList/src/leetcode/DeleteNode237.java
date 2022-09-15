package leetcode;

public class DeleteNode237 {
    public void deleteNode(ListNode node) {

        ListNode succ = node.next;
        node.val = succ.val;

        node.next = succ.next;
        succ.next = null;
    }
}
