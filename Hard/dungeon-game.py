Hard/dungeon-game.py

# Notes:
# - DP
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        path_cost = {}
        # Base case: princess cell (bottom-right)
        # Need at least 1 HP, minus whatever damage/health is in the room
        path_cost[(m-1, n-1)] = max(1, 1 - dungeon[m-1][n-1])

        # Fill the last column (moving upwards)
        for i in range(m-2, -1, -1):
            # Health needed = health needed for the room below - current room value
            path_cost[(i, n-1)] = max(1, path_cost[(i+1, n-1)] - dungeon[i][n-1])

        # Fill the last row (moving leftwards)
        for j in range(n-2, -1, -1):
            # Health needed = health needed for the room to the right - current room value
            path_cost[(m-1, j)] = max(1, path_cost[(m-1, j+1)] - dungeon[m-1][j])
            
        # Fill in the rest of the grid backwards
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                # Pick the path that requires LESS health to survive (down or right)
                next_step_min = min(path_cost[(i+1, j)], path_cost[(i, j+1)])
                path_cost[(i, j)] = max(1, next_step_min - dungeon[i][j])
        
        # The answer is the health needed at the very start
        return path_cost[(0, 0)]
