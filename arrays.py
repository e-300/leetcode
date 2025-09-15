
# def containsDuplicate(nums):
#    """
#    :type nums: List[int]
#    :rtype: bool
#    """
#    #strategy check the length of nums with len of set of nums and if its different then duplicates are there

#    if len(set(nums)) < len(nums):
#       return True
#    else:
#       return False

      
   

# # Test cases
# if __name__ == "__main__":
#    # Example 1
#    nums1 = [1, 2, 3, 1]
#    result1 = containsDuplicate(nums1)
#    print(f"Input: nums = {nums1}")
#    print(f"Output: {result1}")
   
#    # Example 2
#    nums2 = [1, 2, 3, 4]
#    result2 = containsDuplicate(nums2)
#    print(f"Input: nums = {nums2}")
#    print(f"Output: {result2}")
   
#    # Example 3
#    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
#    result3 = containsDuplicate(nums3)
#    print(f"Input: nums = {nums3}")
#    print(f"Output: {result3}")



# def missingNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     return sum(range(0,len(nums)+1)) - sum(nums)



# # Test cases
# if __name__ == "__main__":
#    # Example 1
#    nums1 = [3, 0, 1]
#    result1 = missingNumber(nums1)
#    print(f"Input: nums = {nums1}")
#    print(f"Output: {result1}")
   
#    # Example 2
#    nums2 = [0, 1]
#    result2 = missingNumber(nums2)
#    print(f"Input: nums = {nums2}")
#    print(f"Output: {result2}")
   
#    # Example 3
#    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
#    result3 = missingNumber(nums3)
#    print(f"Input: nums = {nums3}")
#    print(f"Output: {result3}")


# from typing import List

# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         return sum(nums)
        

# # Test cases
# if __name__ == "__main__":
#     solution = Solution()
    
#     # Test case 1
#     nums1 = [4,3,2,7,8,2,3,1]
#     result1 = solution.findDisappearedNumbers(nums1)
#     print(f"Input: {nums1}")
#     print(f"Output: {result1}")
#     print(f"Expected: [5,6]")
#     print()
    
#     # Test case 2
#     nums2 = [1,1]
#     result2 = solution.findDisappearedNumbers(nums2)
#     print(f"Input: {nums2}")
#     print(f"Output: {result2}")
#     print(f"Expected: [2]")
#     print()
    
#     # Test case 3 - Edge case
#     nums3 = [1,2,3,4,5]
#     result3 = solution.findDisappearedNumbers(nums3)
#     print(f"Input: {nums3}")
#     print(f"Output: {result3}")
#     print(f"Expected: []")







# letter_str = "hello"

# def findlet(letter_str):
#     freq_arr = [0]*26

#     for let in letter_str:

#         freq_arr[ord(let) - ord('a')] += 1

#     char_ct = 0

#     letter = 0

#     for i in range(26):
#         if freq_arr[i]  > char_ct:
#             char_ct = freq_arr[i]
#             letter = i
    
#     return chr(letter + ord('a'))



# from typing import List

# def minTimeToVisitAllPoints(points: List[List[int]]) -> int:

#     min_time = 0


#     x1, y1 = points.pop()

#     while(points):

#         x2, y2 = points.pop()
#         min_time += max(abs((x2-x1)),abs((y2-y1)))
#         x1, y1 = x2,y2

#     return min_time
        



# # ----------------------
# # Example test cases
# # ----------------------
# if __name__ == "__main__":
#     print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))  # Expected: 7
#     #print(minTimeToVisitAllPoints([[3,2],[-2,2]]))        # Expected: 5










    
    








# def twoSum(nums, target):
#    """
#    :type nums: List[int]
#    :type target: int
#    :rtype: List[int]
#    """
   
#    pass

# # Test cases
# if __name__ == "__main__":
#    # Example 1
#    nums1 = [2, 7, 11, 15]
#    target1 = 9
#    result1 = twoSum(nums1, target1)
#    print(f"Input: nums = {nums1}, target = {target1}")
#    print(f"Output: {result1}")
   
#    # Example 2
#    nums2 = [3, 2, 4]
#    target2 = 6
#    result2 = twoSum(nums2, target2)
#    print(f"Input: nums = {nums2}, target = {target2}")
#    print(f"Output: {result2}")
   
#    # Example 3
#    nums3 = [3, 3]
#    target3 = 6
#    result3 = twoSum(nums3, target3)
#    print(f"Input: nums = {nums3}, target = {target3}")
#    print(f"Output: {result3}")





# from typing import List

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

#         res = []

#         while matrix:

#             res += matrix.pop(0)



#             for row in matrix:
#                 res.append(row.pop())

#             if matrix:

#                 res += matrix.pop()[::-1]

        
        

#         return res







        # res = []
        # rows = len(matrix)

        # col = len(matrix[0])

        # top_rows = 0
        # bottom_rows = rows-1
        # left_col = 0
        # right_col= col-1



        # while(top_rows <= bottom_rows and left_col <= right_col):

        #     #iter left to right
        #     for cell in range(left_col, right_col+1):
        #         res.append(matrix[top_rows][cell])
        #     top_rows+=1

        #     #itr top to bottom
        #     for cell in range(top_rows,bottom_rows):
        #         res.append(matrix[cell][right_col])
        #     right_col-=1

        #     if top_rows <= bottom_rows:
        #         #itr right to left
        #         for cell in range(right_col, left_col-1, -1):
        #             res.append(matrix[bottom_rows][cell])
        #         bottom_rows-=1

        #     if left_col <= right_col:
        #         #itr bottom to top
        #         for cell in range(bottom_rows, top_rows-1, -1):
        #             res.append(matrix[cell][left_col])
        #         left_col+=1

        # return res
                


        

        

            
            

# # Test cases
# if __name__ == "__main__":
#     solution = Solution()
    
#     # Test case 1
#     matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
#     result1 = solution.spiralOrder(matrix1)
#     expected1 = [1,2,3,6,9,8,7,4,5]
#     print(f"Test 1: {result1} == {expected1} -> {result1 == expected1}")
    
#     # Test case 2
#     matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#     result2 = solution.spiralOrder(matrix2)
#     expected2 = [1,2,3,4,8,12,11,10,9,5,6,7]
#     print(f"Test 2: {result2} == {expected2} -> {result2 == expected2}")
    
#     # Test case 3 - Single row
#     matrix3 = [[1,2,3]]



