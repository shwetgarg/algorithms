import sys
import numpy as np

def min_change(coins, sum):
    min_no_of_coins, coin_to_include = min_change_calc(coins, sum)
    num_coins, final_coins = min_no_of_coins[-1], []
    if num_coins == float('inf'):
        return []
    while sum > 0:
        final_coins.append(coins[coin_to_include[sum]])
        sum -= coins[coin_to_include[sum]]
    return final_coins

def min_change_calc(coins, sum):
    m, n = sum+1, len(coins)
    min_no_of_coins, coin_to_include = [0] * m, [0] * m
    for i in xrange(1, m):
        minNum, minIdx = float('inf'), -1
        for j in xrange(n):
            if coins[j] <= i and 1 + min_no_of_coins[i - coins[j]] < minNum:
                minNum = 1 + min_no_of_coins[i - coins[j]]
                minIdx = j
        min_no_of_coins[i] = minNum
        coin_to_include[i] = minIdx
    return (min_no_of_coins, coin_to_include)
    
sum = int(sys.stdin.readline())
coins = []
while 1:
    try:
        coins.append(int(sys.stdin.readline()))
    except KeyboardInterrupt:
        break
        
final_coins = min_change(coins,sum)
print final_coins
