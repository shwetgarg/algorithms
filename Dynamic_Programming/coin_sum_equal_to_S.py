'''Given a list of N coins, their values (V1, V2, ... VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or report that it's not possible to select coins in such a way that they sum up to S. '''

import sys
import numpy as np

def get_no_of_ways(sum, coins):	
	no_of_ways = [1] + [0]*sum	

	for coin in coins:
		for i in range(coin,sum+1):
			no_of_ways[i] += no_of_ways[i-coin]	

	return no_of_ways[sum]

def get_min_no_of_coins_required(sum, coins):	
	min_no_of_coins = [0] + [sys.maxint]*sum	

	for coin in coins:
		for i in range(coin,sum+1):
			if (min_no_of_coins[i-coin]+1 < min_no_of_coins[i]):
				min_no_of_coins[i] = min_no_of_coins[i-coin]+1

	if (min_no_of_coins[sum] == sys.maxint):
		return "not possible"
	else:
		return min_no_of_coins[sum] 

# Driver program
def main():
	# Case 1:
	print "............Case 1.............."
	sum = 5
	coins = [1,2,5,3]
	no_of_ways = get_no_of_ways(sum, coins)
	print "No of ways: " + str(no_of_ways)
	min_no_of_coins = get_min_no_of_coins_required(sum, coins)
	print "Minimum no of coins: " + str(min_no_of_coins)	
	
	# Case 2:
	print "\n............Case 2.............."
	sum = 5
	coins = [6]
	no_of_ways = get_no_of_ways(sum, coins)
	print "No of ways: " + str(no_of_ways)
	min_no_of_coins = get_min_no_of_coins_required(sum, coins)
	print "Minimum no of coins: " + str(min_no_of_coins)	
        
        
if __name__ == "__main__":
    main()

