from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        nums = sorted(nums)



        l = 0
        r = len(nums)-1
        minlen = 0

        while l <= r:


            if nums[r] == target or nums[l] == target:
                minlen = 1

            current_sum = nums[r] + nums[l]

            if current_sum == target:
                minlen = r - l +1

            if current_sum > target:
                r-=1

            else:            
                l+=1

           

        


        return minlen
        
        

     
        







# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    target1 = 7
    nums1 = [2, 3, 1, 2, 4, 3]
    print(f"Test 1: target={target1}, nums={nums1}")
    print(f"Output: {solution.minSubArrayLen(target1, nums1)}")
    print(f"Expected: 2")
    print()
    
    # Test case 2
    target2 = 4
    nums2 = [1, 4, 4]
    print(f"Test 2: target={target2}, nums={nums2}")
    print(f"Output: {solution.minSubArrayLen(target2, nums2)}")
    print(f"Expected: 1")
    print()
    
    # Test case 3
    target3 = 11
    nums3 = [1, 1, 1, 1, 1, 1, 1, 1]
    print(f"Test 3: target={target3}, nums={nums3}")
    print(f"Output: {solution.minSubArrayLen(target3, nums3)}")
    print(f"Expected: 0")