# Question 4
# time: O(R * C)    R = len(grid), C = len(grid[0]))
# space: O(1)


class Solution4:
    def unique_path(self, obstacleGrid):
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        for i in range(1, r):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)

        for j in range(1, c):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1)

        for i in range(1, r):
            for j in range(1, c):
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1] if obstacleGrid[i][j] == 0 else 0

        return obstacleGrid[r - 1][c - 1]
