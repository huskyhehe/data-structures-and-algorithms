# https://leetcode.com/problems/serialize-and-deserialize-bst/

from Node import TreeNode


class Codec:
    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [root.val] if root else []

    def int_to_str(self, x):
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str

    def serialize(self, root):
        lst = [self.int_to_str(x) for x in self.postorder(root)]
        return ''.join(map(str, lst))

    def str_to_int(self, bytes_str):
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result

    def deserialize(self, data):
        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        n = len(data)
        data = [self.str_to_int(data[4 * i : 4 * i + 4]) for i in range(n // 4)]
        return helper()
