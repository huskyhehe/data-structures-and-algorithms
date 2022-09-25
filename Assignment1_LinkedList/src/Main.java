import model.ListNode;

public class Main {
    public static void main(String[] args) {
        /**
         * Question 1: Rotate List
         */
        Solution1 solution1 = new Solution1();
        System.out.println("---------- Q1 Rotate List ----------");

         // Test Case 1
         // input: 1 -> 2 -> 3 -> 4 -> 5 -> null, 2
        ListNode solution1Head1 = new ListNode(1);
        solution1Head1.next = new ListNode(2);
        solution1Head1.next.next = new ListNode(3);
        solution1Head1.next.next.next = new ListNode(4);
        solution1Head1.next.next.next.next = new ListNode(5);
        // expected output: 4 -> 5 -> 1 -> 2 -> 3 -> null
        printSinglyLinkedList(solution1.rotateRight(solution1Head1, 2));

        // Test Case 2
        // input: 7 -> 8 -> 9 -> null, 5
        ListNode solution1Head2 = new ListNode(7);
        solution1Head2.next = new ListNode(8);
        solution1Head2.next.next = new ListNode(9);
        // expected output: 8 -> 9 -> 7 -> null
        printSinglyLinkedList(solution1.rotateRight(solution1Head2, 5));

        // Test Case 3 (Edge Case)
        // input: 3 -> null, 3
        ListNode solution1Head3 = new ListNode(3);
        // expected output: 3 -> null
        printSinglyLinkedList(solution1.rotateRight(solution1Head3, 3));


        /**
         * Question 2: Remove Elements
         */
        Solution2 solution2 = new Solution2();
        System.out.println("-------- Q2 Remove Elements --------");

        // Test Case 1
        // input: 1 -> 2 -> 6 -> 3 -> 6 -> null, 6
        ListNode solution2Head1 = new ListNode(1);
        solution2Head1.next = new ListNode(2);
        solution2Head1.next.next = new ListNode(6);
        solution2Head1.next.next.next = new ListNode(3);
        solution2Head1.next.next.next.next = new ListNode(6);
        // expected output: 1 - > 2 - > 3 - > null
        printSinglyLinkedList(solution2.removeElements(solution2Head1, 6));

        // Test Case 2
        // input: 7 -> 7 -> 7 -> null, 7
        ListNode solution2Head2 = new ListNode(7);
        solution2Head2.next = new ListNode(7);
        solution2Head2.next.next = new ListNode(7);
        // expected output: null
        printSinglyLinkedList(solution2.removeElements(solution2Head2, 7));

        // Test Case 3 (Edge Case)
        // input: null, 1
        // expected output: null
        printSinglyLinkedList(solution2.removeElements(null, 1));


        /**
         * Question 3: Swap Kth Nodes
         */
        Solution3 solution3 = new Solution3();
        System.out.println("-------- Q3 Swap Kth Nodes ---------");

        // Test Case 1
        // input: 1 -> 4 -> 3 -> 2 -> 5 -> null, 4
        ListNode solution3Head1 = new ListNode(1);
        solution3Head1.next = new ListNode(2);
        solution3Head1.next.next = new ListNode(3);
        solution3Head1.next.next.next = new ListNode(4);
        solution3Head1.next.next.next.next = new ListNode(5);
        // expected output: 1 -> 2 -> 3 -> 4 -> 5 -> null
        printSinglyLinkedList(solution3.swapNodes(solution3Head1, 4));

        // Test Case 2
        // input: 1 -> 2 -> null, 2
        ListNode solution3Head2 = new ListNode(1);
        solution3Head2.next = new ListNode(2);
        // expected output: 2 -> 1 -> null
        printSinglyLinkedList(solution3.swapNodes(solution3Head2, 2));

        // Test Case 3 (Edge 3)
        // input: 5 -> null, 1
        ListNode solution3Head3 = new ListNode(5);
        // expected output: 5 -> null
        printSinglyLinkedList(solution3.swapNodes(solution3Head3, 1));


        /**
         * Question 5: Insert into a Sorted Circular Linked List
         */
        Solution5 solution5 = new Solution5();
        System.out.println("--- Q5 Insert into a Sorted Circular Linked List ---");

        // Test Case 1 (Edge Case)
        // input: null, 1
        ListNode solution5Head1 = null;
        // expected output: 1 ->
        printCircularLinkedList(solution5.insert(solution5Head1, 1));

        // Test Case 2 (Edge Case)
        // input: 1, 0
        ListNode solution5Head2 = new ListNode(1);
        // expected output: 1 -> 0 ->
        printCircularLinkedList(solution5.insert(solution5Head2, 0));

        // Test Case 3
        // input: input: 3 -> 4 -> 1 ->, 2
        ListNode solution5Head3 = new ListNode(3);
        solution5Head3.next = new ListNode(4);
        solution5Head3.next.next = new ListNode(1);
        solution5Head3.next.next.next = solution5Head3;
        // expected output: 3 -> 4 -> 1 -> 2 ->
        printCircularLinkedList(solution5.insert(solution5Head3, 2));

        // Test Case 4
        // input: input: 3 -> 4 -> 1 ->, 7
        ListNode solution5Head4 = new ListNode(3);
        solution5Head4.next = new ListNode(4);
        solution5Head4.next.next = new ListNode(1);
        solution5Head4.next.next.next = solution5Head4;
        // expected output: 3 -> 4 -> 1 -> 2 ->
        printCircularLinkedList(solution5.insert(solution5Head4, 7));
    }

    public static void printSinglyLinkedList(ListNode head) {
        ListNode cur = head;
        while (cur != null) {
            System.out.print(cur.val + " - > ");
            cur = cur.next;
        }
        System.out.println("null");
    }

    public static void printCircularLinkedList(ListNode head) {
        if (head == null) System.out.println("null");
        System.out.print(head.val + " -> ");
        ListNode cur = head.next;
        while (cur != null && cur != head) {
            System.out.print(cur.val + " -> ");
            cur = cur.next;
        }
        System.out.println();
    }
}
