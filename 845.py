"""
LeetCode 845: Longest Mountain in Array

Problem Description:
You may recall that an array arr is a mountain array if and only if:
- arr.length >= 3
- There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
  - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
  - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array arr, return the length of the longest subarray which is a mountain.
Return 0 if there is no mountain subarray.

Example 1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^4
"""

from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        #return 0 if arr < 3
        if len(arr) < 3:
            return 0
        

        #find peak then expand left and expand right
        #count each time we are expanding

        res = 0
        

        for i in range(1,len(arr)-1):

            if arr[i-1] < arr[i] > arr[i+1]:
                
                l = i
                r = i
                


                while arr[l-1] < arr[l] and l > 0:
                    l-=1
                    
                while r < len(arr)-1 and arr[r] > arr[r+1]:
                    r+=1
                    
                
                res = max(res, r-l+1)

        
        return res




def test_longest_mountain():
    solution = Solution()
    
    # Test cases from the problem
    test_cases = [
        # Example test cases
        ([2,1,4,7,3,2,5], 5),  # Expected: 5
        ([2,2,2], 0),           # Expected: 0
        
        # Additional test cases provided
        ([0,2,0,0,2,0,2,1,1,0,2,1,0,0,1,0,2,1,2,0,1,1,0,2,2,1,2,2,0,0,0,1,0,2,0,0,1,2,0,1,0,2,0,2,0,0,0,0,2,1,0,0,0,0,1,0,2,1,2,2,1,0,0,1,0,2,0,0,0,2,1,0,1,2,1,0,1,0,2,1,0,2,0,2,1,1,2,0,1,0,1,1,1,1,2,1,2,2,2,0], 5),
        ([0,1,2,0], 4),
        ([875,884,239,731,723,685], 4),
        ([2,3,1,2,3,4,5,6], 3),
        ([0], 0),
        ([1,2,3,4,5], 0),
        ([5,4,3,2,1], 0),
        ([0,1,2,3,4,5,4,3,2,1,0], 11),
        
        # Edge cases
        ([], 0),               # Empty array
        ([1], 0),              # Single element
        ([1, 2], 0),           # Two elements
        ([1, 2, 1], 3),        # Minimum mountain
        ([1, 2, 3], 0),        # Only increasing
        ([3, 2, 1], 0),        # Only decreasing
        ([1, 3, 2], 3),        # Simple mountain
        ([0,1,2,3,4,5,4,3,2,1,0], 11),  # Full mountain
    ]
    
    print("Running test cases for LeetCode 845: Longest Mountain in Array")
    print("=" * 60)
    
    for i, (arr, expected) in enumerate(test_cases):
        result = solution.longestMountain(arr)
        
        if expected is not None:
            status = "PASS" if result == expected else "FAIL"
            print(f"Test {i+1:2d}: {status}")
            print(f"  Input:    {arr if len(arr) <= 20 else str(arr[:10]) + '...' + str(arr[-10:])}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
        else:
            print(f"Test {i+1:2d}: RUN")
            print(f"  Input:    {arr if len(arr) <= 20 else str(arr[:10]) + '...' + str(arr[-10:])}")
            print(f"  Result:   {result}")
        print()

if __name__ == "__main__":
    test_longest_mountain()