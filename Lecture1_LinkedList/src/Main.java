public class Main {

    public static void main(String[] args) {

        // Integer LinkedList Test Case
        LinkedList<Integer> list1 = new LinkedList<>();
        list1.addNodeToHead(5);
        list1.addNodeToHead(6);
        list1.addNodeToHead(4);
        list1.addNodeToHead(8);
        list1.addNodeToHead(-3);
        list1.addNodeToHead(-2);

        list1.printLinkedList();
        System.out.println(list1.getLength());

        // String LinkedList Test Case
        LinkedList<String> list2 = new LinkedList<>();
        list2.addNodeToTail("ashish");
        list2.addNodeToTail("is");
        list2.addNodeToTail("the");
        list2.addNodeToTail("professor");
        list2.addNodeToTail("of");
        list2.addNodeToTail("INFO6205");

        list2.printLinkedList();
        System.out.println(list2.getLength());

        // Null LinkedList Test Case
        LinkedList<Integer> list3 = new LinkedList<>();
        list3.printLinkedList();
        System.out.println(list3.getLength());
    }
}
