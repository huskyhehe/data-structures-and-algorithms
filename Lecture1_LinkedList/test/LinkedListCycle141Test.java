import leetcode.LinkedListCycle141;
import leetcode.ListNode;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class LinkedListCycle141Test {

    @Test
    public void testHasCycle_pos1() {
        LinkedListCycle141 list = new LinkedListCycle141();
        ListNode head = new ListNode(3);
        ListNode node1 = new ListNode(2);
        head.next = node1;
        head.next.next = new ListNode(0);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = node1;
        Assertions.assertEquals(true, list.hasCycle(head));
    }

    @Test
    public void testHasCycle_pos0() {
        LinkedListCycle141 list = new LinkedListCycle141();
        ListNode head = new ListNode(1);
        ListNode node1 = new ListNode(2);
        head.next = node1;
        node1.next = head;
        Assertions.assertEquals(true, list.hasCycle(head));
    }

    @Test
    public void testHasCycle_no_cycle() {
        LinkedListCycle141 list = new LinkedListCycle141();
        ListNode head = new ListNode(1);
        Assertions.assertEquals(false, list.hasCycle(head));
    }
}
