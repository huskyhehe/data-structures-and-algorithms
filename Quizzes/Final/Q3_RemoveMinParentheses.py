# Question 3
# time: O(N)
# space: O(N)

class Solution3:
    def remove_min_parentheses(self, s):
        stack = []
        surplus = set()

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if not stack:
                    surplus.add(i)
                else:
                    stack.pop()

        surplus = surplus.union(set(stack))

        res = []
        for i, ch in enumerate(s):
            if i not in surplus:
                res.append(ch)

        return "".join(res)
