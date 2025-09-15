from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       # L R
        [7,1,5,3,6,4]

        #two pointer greedy method 
        l = 0
        r = 1

        profit = 0

        while r < len(prices):

            if prices[l] >  prices[r]:
                l = r
            elif prices[r]-prices[l] > profit:
                profit = prices[r]-prices[l] 
            
            r+=1



        return profit


# Test cases
def test_max_profit():
    solution = Solution()
    
    # Test case 1: Normal case with profit possible
    prices1 = [7,1,5,3,6,4]
    result1 = solution.maxProfit(prices1)
    expected1 = 5  # Buy at 1, sell at 6
    print(f"Test 1 - Prices: {prices1}")
    print(f"Expected: {expected1}, Got: {result1}")
    print(f"Pass: {result1 == expected1}\n")
    
    # Test case 2: Decreasing prices - no profit possible
    prices2 = [7,6,4,3,1]
    result2 = solution.maxProfit(prices2)
    expected2 = 0  # No profit possible
    print(f"Test 2 - Prices: {prices2}")
    print(f"Expected: {expected2}, Got: {result2}")
    print(f"Pass: {result2 == expected2}\n")


if __name__ == "__main__":
    test_max_profit()