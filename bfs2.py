from typing import List

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #find location of  rotten oranges 
        #find number of fresh oranges

        rows = len(grid)
        cols = len(grid[0])
        fresh_org = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:

                    fresh_org+=1

                if grid[r][c] == 2:
                    q.append((r,c))

        #if no rotten org 
        if not len(q) > 0:
            return -1
        

        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        mins = 0

        
        #bfs
        while q and fresh_org > 0:

            mins+=1

            current_generation_size = len(q)


            #preform bfs on all rotten oragnes in current level
            while current_generation_size > 0:

                #remove first rotten and start bfs 
                r, c = q.popleft()

                current_generation_size-=1

                for dr,dc in directions:
                    i = r + dr
                    j = c + dc

                    if (i in range(rows) and j in range(cols) ) and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh_org-=1
                        q.append((i,j))

                


        #no fresh oranges left then return mins passed
        if fresh_org == 0:
            return mins
        

        #if there are fresh oranges left that means we couldnt reach them so then we return -1 
        return -1




        


# Test cases
if __name__ == "__main__":
    from typing import List
    
    solution = Solution()
    
    # Test case 1
    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    print(f"Test 1: {solution.orangesRotting(grid1)}")  # Expected: 4
    
    # Test case 2
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    print(f"Test 2: {solution.orangesRotting(grid2)}")  # Expected: -1
    
    # Test case 3
    grid3 = [[0,2]]
    print(f"Test 3: {solution.orangesRotting(grid3)}")  # Expected: 0