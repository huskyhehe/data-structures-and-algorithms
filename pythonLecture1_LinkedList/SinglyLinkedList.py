class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get_length(self) -> int:
        return self.length

    def add_node_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def add_node_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            self.length += 1

    def print_linkedlist(self):
        if not self.head:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(str(temp.val) + " -> ", end=" ")
                temp = temp.next
            print("NULL")


if __name__ == '__main__':
    # add node to head
    list1 = SinglyLinkedList()
    list1.add_node_to_head(4)
    list1.add_node_to_head(7)
    list1.add_node_to_head(8)
    list1.add_node_to_head(-3)
    list1.print_linkedlist()

    # add node to tail
    list2 = SinglyLinkedList()
    list2.add_node_to_tail("Ashish")
    list2.add_node_to_tail("is")
    list2.add_node_to_tail("the")
    list2.add_node_to_tail("professor")
    list2.add_node_to_tail("of")
    list2.add_node_to_tail("INFO6205")
    list2.print_linkedlist()
