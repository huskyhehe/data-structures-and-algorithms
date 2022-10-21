# https://leetcode.com/problems/all-paths-from-source-to-target/

# time: O(2^n * n)
# space: O(n)

from typing import List


class Solution8:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph) - 1

        def backtrack(cur_node: int, path: List[int]) -> None:
            if cur_node == target:
                res.append(path[:])
                return

            for next_node in graph[cur_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        backtrack(0, [0])
        return res



