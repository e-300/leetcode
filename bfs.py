"""
LeetCode 200: Number of Islands

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.
"""

from typing import List

from collections import deque

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        def bfs(r, c):

            queue = deque()
            visit.add((r,c))
            queue.append((r,c))
            
            while queue:

                directions = [[-1,0],[1,0],[0,1],[0,-1]]

                row, col = queue.popleft()

                for d in directions:
                    dr, dc = d

                    r = row+dr
                    c = col+dc

                    if (r in range(rows)and (c in range(cols)) and grid[r][c] == '1' and (r,c) not in visit):
                        queue.append((r,c))
                        visit.add((r,c))

        visit = set()
        count = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r, c)
                    count+=1
        

        return count



# Test cases
def test_numIslands():
    solution = Solution()
    
    # Test case 1
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    expected1 = 1
    result1 = solution.numIslands(grid1)
    print(f"Test 1: Expected {expected1}, Got {result1}, {'PASS' if result1 == expected1 else 'FAIL'}")
    
    # Test case 2
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    expected2 = 3
    result2 = solution.numIslands(grid2)
    print(f"Test 2: Expected {expected2}, Got {result2}, {'PASS' if result2 == expected2 else 'FAIL'}")
    
    # Test case 3: Single cell island
    grid3 = [["1"]]
    expected3 = 1
    result3 = solution.numIslands(grid3)
    print(f"Test 3: Expected {expected3}, Got {result3}, {'PASS' if result3 == expected3 else 'FAIL'}")
    
    # Test case 4: No islands
    grid4 = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    expected4 = 0
    result4 = solution.numIslands(grid4)
    print(f"Test 4: Expected {expected4}, Got {result4}, {'PASS' if result4 == expected4 else 'FAIL'}")
    
    # Test case 5: All islands
    grid5 = [
        ["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]
    ]
    expected5 = 1
    result5 = solution.numIslands(grid5)
    print(f"Test 5: Expected {expected5}, Got {result5}, {'PASS' if result5 == expected5 else 'FAIL'}")
    
    # Test case 6: Complex pattern
    grid6 = [
        ["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]
    ]
    expected6 = 1
    result6 = solution.numIslands(grid6)
    print(f"Test 6: Expected {expected6}, Got {result6}, {'PASS' if result6 == expected6 else 'FAIL'}")

if __name__ == "__main__":
    test_numIslands()




#ROTTING ORANGES
from collections import deque
class Solution:
    def orangesRotting(self, grid):


        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        count = 0

        fresh_exist = False

        #find all rotten and make sure there are some 1's present
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '2':
                    q.append((row,col))
                 

                if grid[row][col] == '1':
                    fresh_exist = True


        #no fresh oranges
        if not fresh_exist:
            return 0
    

        #if there are no rotting orangess
        if len(q) == 0 and fresh_exist:
            return -1

        
        #bfs
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        #initialize mins
        mins = 0

        while q:
            
            #level size is the length of the queue
            level_size = len(q)
            while level_size != 0:
                r,c = q.popleft()
                min+=1
                for dr, dc in directions:
                    r = r+dr
                    c = c+dc
                    if(r in range(rows) and c in range(cols) and grid[r][c] == '1'):
                        q.append((r,c))
                        grid[r][c] = '2'
            level_size-=1
            

        #if there are remaining fresh oranges that couldnt be reached then return -1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    return -1
                    

        return mins
        




# Test cases
def test_rotting_oranges():
    solution = Solution()
    
    # Test case 1
    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    result1 = solution.orangesRotting(grid1)
    print(f"Test 1 - Grid: {grid1}")
    print(f"Expected: 4, Got: {result1}")
    print()
    
    # Test case 2
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    result2 = solution.orangesRotting(grid2)
    print(f"Test 2 - Grid: {grid2}")
    print(f"Expected: -1, Got: {result2}")
    print()


if __name__ == "__main__":
    test_rotting_oranges()