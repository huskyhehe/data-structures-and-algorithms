# Question2
# time: O(R * C)    R = len(grid), C = len(grid[0]))
# space: O(R * C)

class Solution2:
    def num_of_islands(self, grid):
        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + direction[0], c + direction[1])

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count
