public class LinkedList <T> {

    private Node<T> head;
    private int length;

    public LinkedList() {
        this.head = null;
        this.length = 0;
    }

    public int getLength() {
        return length;
    }


    public void addNodeToHead(T data) {
        Node<T> addNode = new Node<>(data);
        addNode.next = head;
        head = addNode;
        length ++;
    }


    public void addNodeToTail(T data) {
        Node<T> addNode = new Node<>(data);

        if (head == null) {
            head = addNode;
        } else {
            Node<T> temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = addNode;
        }
        length ++;
    }


    public void printLinkedList() {
        if (head == null) {
            System.out.println("List is empty");
        } else {
            Node<T> temp = head;
            while (temp != null) {
                System.out.print(temp.data + " -> ");
                temp = temp.next;
            }
            System.out.println("NULL");
        }
    }
}
