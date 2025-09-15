class Solution:
    def twoSum(self, numbers, target):


        l = 0
        r = len(numbers)-1
        res = []

        while l < r:

            cs = numbers[l] + numbers[r]

            if cs > target:
                r-=1
            elif cs < target:
                l+=1
            else:
                res.append(l+1)
                res.append(r+1)
                break

        return res
    




# Test cases
solution = Solution()

# Test case 1
numbers1 = [2,7,11,15]
target1 = 9
expected1 = [1,2]
result1 = solution.twoSum(numbers1, target1)
print(f"Test 1: tested: {numbers1} \n{result1} == {expected1} -> {result1 == expected1}")

# Test case 2
numbers2 = [2,3,4]
target2 = 6
expected2 = [1,3]
result2 = solution.twoSum(numbers2, target2)
print(f"Test 2: tested: {numbers2} \nResult {result2} == {expected2} -> {result2 == expected2}")

# Test case 3
numbers3 = [-1,0]
target3 = -1
expected3 = [1,2]
result3 = solution.twoSum(numbers3, target3)
print(f"Test 3: tested: {numbers3} \nResult {result3} == {expected3} -> {result3 == expected3}")

# Test case 4
numbers4 = [1,2,3,4,4,9,56,90]
target4 = 8
expected4 = [4,5]
result4 = solution.twoSum(numbers4, target4)
print(f"Test 4: tested: {numbers4} \nResult {result4} == {expected4} -> {result4 == expected4}")

# Test case 5
numbers5 = [5,25,75]
target5 = 100
expected5 = [2,3]
result5 = solution.twoSum(numbers5, target5)
print(f"Test 5: tested: {numbers5} \nResult {result5} == {expected5} -> {result5 == expected5}")

