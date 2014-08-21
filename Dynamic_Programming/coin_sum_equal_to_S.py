import sys
import numpy as np

def get_no_of_ways(sum, coins):	
	no_of_ways = [1] + [0]*sum	

	for coin in coins:
		for i in range(coin,sum+1):
			no_of_ways[i] += no_of_ways[i-coin]	

	return no_of_ways

def get_min_no_of_coins_required(sum, coins):	
	min_no_of_coins = [0] + [10000000]*sum	

	for coin in coins:
		for i in range(coin,sum+1):
			if (min_no_of_coins[i-coin]+1 < min_no_of_coins[i]):
				min_no_of_coins[i] = min_no_of_coins[i-coin]+1

	return min_no_of_coins

def main():
	sum = 5
	coins = [1, 3, 2, 5]
	no_of_ways = get_no_of_ways(sum, coins)
	print "No of ways: " + str(no_of_ways[sum])
	min_no_of_coins = get_min_no_of_coins_required(sum, coins)
	print "Minimum no of coins: " + str(min_no_of_coins[sum])	
        
if __name__ == "__main__":
    main()

