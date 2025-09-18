"""
1200. Minimum Absolute Difference

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order (with respect to pairs), each pair [a, b] follows:
- a, b are from arr
- a < b
- b - a equals to the minimum absolute difference of any two elements in arr

Constraints:
- 2 <= arr.length <= 10^5
- -10^6 <= arr[i] <= 10^6
"""

class Solution:
    # def minimumAbsDifference(self, arr):

    #     arr = sorted(arr)

    #     minDiff = float('inf')


    #     for i in range(1,len(arr)):

    #         minDiff = min(minDiff, arr[i] - arr[i-1])

    #     res = []

    #     for i in range(1,len(arr)):

    #         if arr[i] - arr[i-1] == minDiff:
    #             res.append([arr[i-1],arr[i]])

        
    #     return res
    

    #O(n) solution

    # Iterate through all the possible d =  1 - (max(arr) - min(arr))
    # use set to check if any numbers with the current distance iteration have any partners that exactly d away
    # pairs that make the above true are pairs store them in res 
    # if no pairs then loop continues
    # this is shit I can do better

    # def minimumAbsDifference(self, arr):

    #     seen = set(arr)

    #     res = []

    #     for distance in range(1, (max(arr)-min(arr))+1):

    #         for num in range(min(arr), max(arr)+1):
                    
    #             if num in seen:
    #                 if num + distance in seen:
    #                     res.append([num,num+distance])
                
    #         if res:
    #             return res
            
    #     return res



    # Better O(N) solution!
    # Use counting sort to sort the arr 
    # Then we can use the same method used in our n log n solution to build our res arr!



    def minimumAbsDifference(self,arr):
        if len(arr) < 2:
            return []

        # Use counting sort only if range is reasonable
        min_val = min(arr)
        max_val = max(arr)
        range_size = max_val - min_val + 1

        if range_size > len(arr) * 2:
            sorted_arr = sorted(arr)
        else:
            min_val = min(arr)

            max_val = max(arr)

            range_size = max_val - min_val + 1

            # Initialize count
            count = [0] * range_size

            # Count frequencies, offset by min_val
            for num in arr:
                count[num - min_val] += 1

            # Calculate cumulative positions
            for i in range(1, range_size):
                count[i] += count[i - 1]

            # Place elements in sorted order
            sorted_arr = [0] * len(arr)

            for i in range(len(arr) - 1, -1, -1):
                val = arr[i]
                pos = count[val - min_val] - 1
                sorted_arr[pos] = val
                count[val - min_val] -= 1

        # Single pass to find minimum difference and collect pairs
        minDiff = float('inf')
        res = []

        for i in range(1, len(sorted_arr)):
            diff = sorted_arr[i] - sorted_arr[i-1]

            if diff < minDiff:
                minDiff = diff
                res = [[sorted_arr[i-1], sorted_arr[i]]]
                if minDiff == 0:
                    break
            elif diff == minDiff:
                res.append([sorted_arr[i-1], sorted_arr[i]])

        return res







                    

                





                        







        
        







        

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    arr1 = [4, 2, 1, 3]
    print(f"Input: {arr1}")
    print(f"Output: {solution.minimumAbsDifference(arr1)}")
    print(f"Expected: [[1,2],[2,3],[3,4]]")
    print()
    
    # Test case 2
    arr2 = [1, 3, 6, 10, 15]
    print(f"Input: {arr2}")
    print(f"Output: {solution.minimumAbsDifference(arr2)}")
    print(f"Expected: [[1,3]]")
    print()
    
    # Test case 3
    arr3 = [3, 8, -10, 23, 19, -4, -14, 27]
    print(f"Input: {arr3}")
    print(f"Output: {solution.minimumAbsDifference(arr3)}")
    print(f"Expected: [[-14,-10],[19,23],[23,27]]")
    print()