class LinkedList<T> {
    private var head: Node<T>? = null
    var length = 0
        private set

    fun addNodeToHead(data: T) {
        val addNode = Node(data)
        addNode.next = head
        head = addNode
        length++
    }

    fun addNodeToTail(data: T) {
        val addNode = Node(data)
        if (head == null) {
            head = addNode
        } else {
            var temp: Node<T> = head
            while (temp.next != null) {
                temp = temp.next
            }
            temp.next = addNode
        }
        length++
    }

    fun printLinkedList() {
        if (head == null) {
            println("List is empty")
        } else {
            var temp = head
            while (temp != null) {
                print(temp.data.toString() + " -> ")
                temp = temp.next
            }
            println("NULL")
        }
    }
}