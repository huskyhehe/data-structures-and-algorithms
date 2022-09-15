# LinkedList

The most common variants of linked lists are:

- Singly Linked List
- Doubly Linked List
- Circular Linked List 

All variants refer to how the items (nodes) of the list point to each other. The Singly Linked List will only have one pointer that has a reference to the next node in the list, whereas, the Doubly Linked List would have a pointer to the next item as well as the previous item. In almost ALL interviewing scenarios the linked list will be the Singly Linked List and the rest of the documentation will refer to linked list as that and only the other list types if specifically mentioned.

A minimal, but quite common Python definition of a linked list node would be:

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
```
Create the list 1 -> 2 and 1 is at the head (front) of the list.
```python
head = ListNode(1)
head.next = ListNode(2)
```

## Glossary
- **Node** - a position in a list that contains the value of whatever is stored at the position as well as at least one reference to another node.
- **Head** — node at the beginning of the list.
- **Tail** — node at the end of the list.
- **Sentinel** — a dummy node, typically placed at the head or end of the list to help make operations simpler (e.g., delete) or to indicate the termination of the list.

## Time and Space Complexity
- **Best cases:** Accessing / Search : O(1) Inserting at head: O(1) Deleting at head: O(1)
- **Worst cases:** Accessing / Searching : O(N) Inserting: O(N) Deleting: O(N)

Best Case occurs when the node is at the head of the list and Worst Case is when the node is at the end of the list.
