# 1 Dummy Head Technique
This is a very common linked list technique as it typically saves you creating [special edge condition logic](https://youtu.be/njTh_OwMljA?t=6m35s) in order to operate on the head of a linked list with some algorithms. This technique only involves creating one extra pointer, the dummy head, that will point to your final answer or list that you will return. This technique is much easier to demonstrate with an example.

## Delete Node
Say you are asked to delete a node in a linked list given the value of the node you want to delete. Furthermore you are told that you can assume the values are unique.

For example:
```
Input: 1->2->4, 2
Output: 1->4
```

```python
class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None
    
def delete_node(head, val):
    d = Node("dummy") # 1
    d.next = head
    p = d
    c = head
    while c:
        if c.val == val:
            p.next = c.next # 2
            return d.next   # 3
        p = c
        c = c.next
    return d.next # 4 
```

1. The creation of the dummy head, in this case it is initialized to point to the original list.
2. Because we created the dummy head we don't have to treat deleting the head of the original list any different from other elements in the list.
3. The dummy head points to the answer list so we simply return the next node as the head of the answer.
4. If we don't happen to find the item setting the dummy head to the original list makes it still point to the correct answer.

## Summary
Treating the dummy head with the invariant that it is always pointing to the current correct answer makes dealing with edge cases in linked lists a lot easier and can be found in a number of elegant solutions.

## Reference

* <https://web.archive.org/web/20180227180712/http://www.eternallyconfuzzled.com/tuts/datastructures/jsw_tut_linklist.aspx>

<br/>

# 2 Multiple Pass Technique
Most computations on a list will require O(N) time complexity, so a simple but very useful technique is to pass through the list a constant number of times to calculate some summary of the list that will simplify your algorithm. One example that we see a lot is the need to calculate the length of the list. That sounds simple enough, but let's see an example to motivate this technique better.

## Example: Intersection of Two Linked Lists
Let's take a look at this common problem as defined in [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists).
> Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
```
begin to intersect at node c1.

>Notes:
- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.
- Your code should preferably run in O(n) time and use only O(1) memory.

We will not cover the full solution to this problem here, but instead cover two insights that can make the solution much simpler. The first insight is that once a list has intersected with another list the rest of the list is identical. Next, a list can only be identical if it is the same length. With these insights a strawman solution is to ignore any prefix of the longer of the two lists because it can't be part of the intersection. The rest of the algorithm also flows much easier after that. So let's just take the sub-task of taking two lists of any length and returning references to two lists of the same length. In the example above it would be lists starting at `a1` and `b2`.

```python
class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None

    def __repr__(self):
        return f"{self.val} --> {self.next}"

    def insert(self, v):
        n = Node(v)
        n.next = self
        return n

def get_len(ll):
    l = 0
    while ll:
        l += 1
        ll = ll.next
    return l

def make_same_length(ll1, ll2):
    len1 = get_len(ll1)
    len2 = get_len(ll2)
    if len1 > len2:
        long_ll, short_ll = ll1, ll2
        long_len, short_len = len1, len2
    else:
        long_ll, short_ll = ll2, ll1
        long_len, short_len = len2, len1
    while long_len > short_len:
        long_len -= 1
        long_ll = long_ll.next
    return short_ll, long_ll

common = Node('c1')
short = common.insert('a2').insert('a1')
long = common.insert('b3').insert('b2').insert('b1')
make_same_length(short, long)
```

### Output:
```python
"(a1 --> a2 --> c1 --> None, b2 --> b3 --> c1 --> None)"
```

### Aside: Recursion vs. Iteration
Let's take an opportunity to use the length calculation to demonstrate recursive vs. iterative solutions. Recursive algorithms are often very easy to write with linked lists because the list is structured recursively.

```python
def get_len_recur(ll):
    if not ll: return 0 # A None path has 0 length
    return get_len_recur(ll.next) + 1 # The length at this node is 1 + length of rest

def get_len_iter(ll):
    l = 0
    while ll:
        l += 1
        ll = ll.next
    return l

get_len_recur(long), get_len_iter(long)
```

#### Output:
```python
(4, 4)
```

The recursive length calculation has three parts to the function:
1) What to return in the "base" case? I.e., the None value has length 0
2) Given any node of the path, how to calculate the length of the path from that node until the end?
3) How to relate the desired answer to the final recursive computation? In this case, it is exactly equal to the final recursive computation so we just return the computation.

The recursive algorithm reads more simply because the looping is not explicitly written, i.e., the `while ll` line in the iterative algorithm. Unfortunately for recursion, this is also the major drawback of the recursive algorithm. The looping is implicitly done for you by the execution of your program, namely every successive call to your recursive function places some data on your call stack and then goes to the next function. For most situations, this means you are paying a storage penalty equal to the size of the list. Some languages can get around this with [tail call](https://en.wikipedia.org/wiki/Tail_call) optimization.

<br/>

# 3 Two Pointers Technique
A very useful technique for dealing with linked lists involves iterating through the list with 2 or more pointers. The differences between how the pointers iterate can be used to make calculations on the list more efficient. This is best demonstrated with an example and probably the most famous example of this technique is cycle detection.

## Detect Cycle in Linked List
Let's use the problem definition of [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle). 
> Given a linked list, determine if it has a cycle in it. Can you do it with constant extra space?

**Answer: Using extra storage time = O(N), space = O(N)**
A cycle can be defined as a list where we point to the same node twice. So the first thing that most people think of is to use another data structure to store nodes that we have already seen as we traverse the list. Then as we move through the nodes of the list we check to see if we have already stored the current node in our auxillary data structure and if we have then we have found a cycle. The typical data structure to choose here is a hash map because it offers constant time insertion and lookup. Here is an acceptable answer:

```python
class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None
        
    def insert(self, n):
        n.next = self
        return n

def has_cycle_with_aux(ll):
    aux = set()
    while ll:
        if ll in aux:
            return True
        aux.add(ll)
        ll = ll.next
    return False

my_list = Node(7).insert(Node(5))
print(f"List {my_list.val} --> {my_list.next.val} --> {my_list.next.next}")
print(has_cycle_with_aux(my_list))
my_list.next.next = my_list
print(f"List {my_list.val} --> {my_list.next.val} --> {my_list.next.next.val}")
print(has_cycle_with_aux(my_list))
```

**Output:**
```python
"List 5 --> 7 --> None"
False
"List 5 --> 7 --> 5"
True
```

**Answer: Two Pointers, time = O(N) space = O(1)**
We can get rid of the extra auxillary data structure by utilizing only one additional pointer. We can then use the two pointers to iterate through the list at two different speeds. The motivation being that if there is a cycle, then the list can be thought of as a circle (at least the part of the list past the self-intersection). Similar to a race track, the faster pointer must eventually cross paths with the slower pointer, whereas if there is not a cycle they will never cross paths.

```python
def has_cycle(ll):
    if not ll or not ll.next:
        return False
    fp = ll.next
    sp = ll
    while fp and fp.next:
        if fp == sp or fp.next == sp:
            return True
        fp = fp.next.next
        sp = sp.next
    return False

my_list = Node(7).insert(Node(5))
print(f"List {my_list.val} --> {my_list.next.val} --> {my_list.next.next}")
print(has_cycle(my_list))
my_list.next.next = my_list
print(f"List {my_list.val} --> {my_list.next.val} --> {my_list.next.next.val}")
print(has_cycle(my_list)) 
```

#### Output:
```python
"List 5 --> 7 --> None"
False
"List 5 --> 7 --> 5"
True
```


Race Car Algorithm Illustration
The race car algorithm detects cycles in a linked list by simultaneously iterating a fast pointer which moves two nodes at a time and a slow pointer which moves one node at a time. If the linked list has no cycles, then the fast pointer will reach NULL, and the algorithm returns false.


![Step_No_Cycle](https://i.imgur.com/3xoVrtS.png)
![Start_No_Cycle](https://i.imgur.com/zYNHIFP.png)

In the case of a cycle, both pointers will get stuck in the cycle, and the fast pointer will eventually lap the slow pointer. As the fast pointer is lapping the slow pointer, it will eventually either be pointing at the same node as the slow pointer, or be pointing at the slow pointer's previous node. In the latter case, the fast pointer will point at the same node as the slow pointer in the next iteration. When the two pointers point at the same node, the algorithm returns true.

![Start_With_Cycle](https://i.imgur.com/fo0YqIF.png)
![Step_With_Cycle](https://i.imgur.com/JmLb8qW.png)
