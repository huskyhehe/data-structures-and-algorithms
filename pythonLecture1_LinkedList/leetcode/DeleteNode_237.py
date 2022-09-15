class Solution:
    def deleteNode(self, node):
        succ = node.next
        node.val = succ.val

        node.next = succ.next
        succ.next = None
