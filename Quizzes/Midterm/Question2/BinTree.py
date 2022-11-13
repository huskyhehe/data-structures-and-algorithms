"""
Question
Populate parent of each node. in the binary tree
"""

# time: O(n)

class BinTree:
    def __init__(self, root=None):
        self.root = root

    def populateParent(self, root):
        if not root:
            return
        self.populateParent(root.left)
        if root.left:
            self.root.left.parent = root
        if root.right:
            self.root.right.parent = root
        self.populateParent(root.right)



















    function inOrderSuccessor(node){
   if(!node) return

   if(node.right){
     let current = node.right
     while(current && current.left) current = current.left
     return current
   }

   let parent = node.parent

   while(parent && parent.right === node) {
     root = node.parent
     parent = parent.parent
   }

   if(!parent) return null

   return parent
}













    def findParent(node : Node, val : int, parent : int) -> None:
        if (node is None):
            return

        if (node.data == val):
            # Print its parent
            print(parent)
        else:

            # Recursive calls
            # for the children
            # of the current node
            # Current node is now
            # the new parent
            findParent(node.left,
                       val, node.data)
            findParent(node.right,
                       val, node.data)



