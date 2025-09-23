from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        left = 0

        curr_sum = 0

        min_lenth = float('inf')


        for right in range(len(nums)):

            curr_sum += nums[right]

            while curr_sum >= target:

                #print(f"minlen{min_lenth}\nright{right}\nleft{left}\ncurrentsum{curr_sum}")

                min_lenth = min(min_lenth, right-left+1)
                curr_sum-=nums[left]
                left+=1


        if min_lenth != float('inf'):
            return min_lenth

        return 0





        


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