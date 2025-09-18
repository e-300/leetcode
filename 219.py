#contains duplicate 2



from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = set()

        for i, num in enumerate(nums):

            if num in seen:
                return True
            
            seen.add(num)

            if len(seen) > k:
                seen.remove(nums[i-k])

        return False








# Test cases
if __name__ == "__main__":
    from typing import List
    
    solution = Solution()
    
    # Test case 1
    q1 = [1,2,3,1]
    print(f"Test 1: {solution.containsNearbyDuplicate(q1,3)}")  # Expected: True
    
    # Test case 2
    q2 = [1,0,1,1]
    print(f"Test 2: {solution.containsNearbyDuplicate(q2, 1)}")  # Expected: True
    
    # Test case 3
    q3 = [1,2,3,1,2,3]
    print(f"Test 3: {solution.containsNearbyDuplicate(q3, 2)}")  # Expected: False





