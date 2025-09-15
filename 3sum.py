from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return nums


        nums = sorted(nums)


        res = []


        for i in range(len(nums)-2):

            #skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue            

            left = i+1

            right = len(nums)-1

            

            while left < right:

                curr_sum = nums[i] + nums[left] + nums[right]

                

                if curr_sum > 0:
                    right -= 1

                    
                elif curr_sum < 0: 
                    left += 1
                
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1

                    while (left<right) and (nums[left] == nums[left-1]):
                        left+=1
                    
                

        return res


        


# Test Cases
def test_three_sum():
    solution = Solution()
    
    # Test Case 1: Basic example with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    result1 = solution.threeSum(nums1)
    print(f"Test 1: {result1}")
    print(f"Expected: {expected1}")
    print(f"Pass: {sorted(result1) == sorted(expected1)}\n")
    
    # Test Case 2: No valid triplets
    nums2 = [0, 1, 1]
    expected2 = []
    result2 = solution.threeSum(nums2)
    print(f"Test 2: {result2}")
    print(f"Expected: {expected2}")
    print(f"Pass: {result2 == expected2}\n")
    
    # Test Case 3: All zeros
    nums3 = [0, 0, 0]
    expected3 = [[0, 0, 0]]
    result3 = solution.threeSum(nums3)
    print(f"Test 3: {result3}")
    print(f"Expected: {expected3}")
    print(f"Pass: {result3 == expected3}\n")
    
    # Test Case 4: Array with duplicates
    nums4 = [-2, 0, 0, 2, 2]
    expected4 = [[-2, 0, 2]]
    result4 = solution.threeSum(nums4)
    print(f"Test 4: {result4}")
    print(f"Expected: {expected4}")
    print(f"Pass: {result4 == expected4}\n")
    
    # Test Case 5: Larger array with multiple solutions
    nums5 = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    result5 = solution.threeSum(nums5)
    print(f"Test 5: {result5}")
    print("Expected multiple valid triplets (manual verification needed)\n")
    
    # Test Case 6: Empty array
    nums6 = []
    expected6 = []
    result6 = solution.threeSum(nums6)
    print(f"Test 6: {result6}")
    print(f"Expected: {expected6}")
    print(f"Pass: {result6 == expected6}\n")
    
    # Test Case 7: Array with less than 3 elements
    nums7 = [1, 2]
    expected7 = []
    result7 = solution.threeSum(nums7)
    print(f"Test 7: {result7}")
    print(f"Expected: {expected7}")
    print(f"Pass: {result7 == expected7}\n")
    
    # Test Case 8: All positive numbers
    nums8 = [1, 2, 3, 4, 5]
    expected8 = []
    result8 = solution.threeSum(nums8)
    print(f"Test 8: {result8}")
    print(f"Expected: {expected8}")
    print(f"Pass: {result8 == expected8}\n")
    
    # Test Case 9: All negative numbers
    nums9 = [-5, -4, -3, -2, -1]
    expected9 = []
    result9 = solution.threeSum(nums9)
    print(f"Test 9: {result9}")
    print(f"Expected: {expected9}")
    print(f"Pass: {result9 == expected9}\n")
    
    # Test Case 10: Edge case with zeros and other numbers
    nums10 = [-2, 0, 1, 1, 2]
    expected10 = [[-2, 0, 2], [-2, 1, 1]]
    result10 = solution.threeSum(nums10)
    print(f"Test 10: {result10}")
    print(f"Expected: {expected10}")
    print(f"Pass: {sorted(result10) == sorted(expected10)}\n")


if __name__ == "__main__":
    test_three_sum()


# Additional helper function to verify solution manually
def verify_triplets(nums, triplets):
    """
    Verify that all triplets are valid (sum to 0 and no duplicates)
    """
    print("Verification:")
    for triplet in triplets:
        print(f"{triplet} -> sum = {sum(triplet)}")
    
    # Check for duplicates
    unique_triplets = set(tuple(sorted(t)) for t in triplets)
    print(f"Original count: {len(triplets)}, Unique count: {len(unique_triplets)}")
    print(f"No duplicates: {len(triplets) == len(unique_triplets)}")


# Example usage for manual testing:
solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
result = solution.threeSum(nums)
verify_triplets(nums, result)