from typing import List

import collections
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        res = collections.deque()

        l_ptr = 0
        r_ptr = len(nums)-1

        
        while l_ptr <= r_ptr:

            #calculate values 
            left_value = abs(nums[l_ptr])
            right_value = abs(nums[r_ptr])

            #if left value less than right append and move pointer up
            if left_value > right_value:
                res.appendleft(left_value*left_value)
                l_ptr +=1

            else:
                res.appendleft(right_value*right_value)
                r_ptr-=1
        
        # res=res[::-1]
        return list(res)


                

            


        

# Test cases
def test_sortedSquares():
    solution = Solution()
    
    # Test case 1
    nums1 = [-4, -1, 0, 3, 10]
    expected1 = [0, 1, 9, 16, 100]
    result1 = solution.sortedSquares(nums1)
    print(f"Test 1: {result1} == {expected1} -> {result1 == expected1} ")
    
    # Test case 2
    nums2 = [-7, -3, 2, 3, 11]
    expected2 = [4, 9, 9, 49, 121]
    result2 = solution.sortedSquares(nums2)
    print(f"Test 2: {result2} == {expected2} -> {result2 == expected2}")
    
    # Test case 3
    nums3 = [-5, -3, -2, -1]
    expected3 = [1, 4, 9, 25]
    result3 = solution.sortedSquares(nums3)
    print(f"Test 3: {result3} == {expected3} -> {result3 == expected3}")

    # Test case 4
    nums4 = [-1, 2, 2]
    expected4 = [1,4,4]
    result4 = solution.sortedSquares(nums4)
    print(f"Test 4: {result4} == {expected4} -> {result4 == expected4}")

    # Test case 5
    nums5 = [0,2]
    expected5 = [0,4]
    result5 = solution.sortedSquares(nums5)
    print(f"Test 4: {result5} == {expected5} -> {result5 == expected5}")


# Uncomment to run tests
test_sortedSquares()






