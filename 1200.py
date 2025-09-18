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



    def minimumAbsDifference(self, arr):

        seen = set(arr)


        res = []

        for distance in range(1, (max(arr)-min(arr))+1):

            for num in range(min(arr), max(arr)+1):
                
                if num + distance in seen:
                    res.append([num,num+distance])
                    
            if res:
                return res
            
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