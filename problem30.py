"""You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""

def maxWater(arr, n) :
	
	res = 0;
	
	for i in range(1, n - 1) :
		
		left = arr[i];
		for j in range(i) :
			left = max(left, arr[j]);
		
		right = arr[i];
		
		for j in range(i + 1 , n) :
			right = max(right, arr[j]);
			
		res = res + (min(left, right) - arr[i]);

	return res;

arr = [3, 0, 1, 3, 0, 5];
n = len(arr);
	
print(maxWater(arr, n));
	


