def coinChange(coins, amount):
    
    dp_array = [float('inf')] * (amount+1)

    dp_array[0] = 0

    #print (dp_array)

    for coin in coins:
        
        print(f"coin {coin}")

        for current_amount in range(coin, amount+1):


            dp_array[current_amount] = min(dp_array[current_amount],dp_array[current_amount-coin]+1)

    
    return dp_array[amount] if dp_array[amount] != float('inf') else -1

# Test Cases
def test_coin_change():
    # Test Case 1
    coins1 = [1, 3, 4]
    amount1 = 6
    result1 = coinChange(coins1, amount1)
    print(f"Test 1 - Input: coins={coins1}, amount={amount1}")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print()
    
    # Test Case 2
    coins2 = [2]
    amount2 = 3
    result2 = coinChange(coins2, amount2)
    print(f"Test 2 - Input: coins={coins2}, amount={amount2}")
    print(f"Output: {result2}")
    print(f"Expected: -1")
    print()
    
    # Test Case 3
    coins3 = [1]
    amount3 = 0
    result3 = coinChange(coins3, amount3)
    print(f"Test 3 - Input: coins={coins3}, amount={amount3}")
    print(f"Output: {result3}")
    print(f"Expected: 0")
    print()

# Run tests
if __name__ == "__main__":
    test_coin_change()