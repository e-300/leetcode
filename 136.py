"""
LeetCode 136: Single Number

Problem Description:
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears exactly twice except for one element which appears exactly once.

Follow-up: Could you implement it without using extra memory?
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # TODO: Implement your solution here
        # Hint: Think about XOR properties
        # XOR properties:
        # a ^ a = 0 (any number XOR with itself is 0)
        # a ^ 0 = a (any number XOR with 0 is the number itself)
        # XOR is commutative and associative

        res = 0

        for num in nums:
            res = res^num

        return res

def test_single_number():
    solution = Solution()
    
    # Test cases
    test_cases = [
        # Example test cases from problem
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        
        # Additional test cases
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([5], 5),
        ([0, 1, 0], 1),
        ([7, 3, 7], 3),
        ([-1, -1, 2], 2),
        ([1, 2, 3, 2, 1], 3),
        
        # Edge cases with negative numbers
        ([-4, 1, 2, 1, 2], -4),
        ([0, 0, 1], 1),
        ([-1], -1),
        
        # Larger arrays
        ([8, 7, 6, 7, 6, 5, 5], 8),
        ([10, 20, 30, 10, 30], 20),
        
        # Test with duplicates at different positions
        ([9, 1, 4, 9, 1, 4, 2], 2),
        ([100, 4, 200, 1, 4, 1, 2, 2, 200], 100),
        
        # Test with zeros
        ([0, 1, 0, 1, 2], 2),
        ([5, 7, 5, 4, 7], 4),
        
        # Sequential numbers
        ([1, 2, 3, 4, 1, 2, 3], 4),
        
        # Large numbers (within constraint bounds)
        ([30000, -30000, 30000], -30000),
        ([-1000, 2000, -1000], 2000),
    ]
    
    print("Running test cases for LeetCode 136: Single Number")
    print("=" * 55)
    
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.singleNumber(nums)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        print(f"Test {i+1:2d}: {status}")
        print(f"  Input:    {nums if len(nums) <= 15 else str(nums[:7]) + ' ... ' + str(nums[-7:])}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print()

if __name__ == "__main__":
    test_single_number()