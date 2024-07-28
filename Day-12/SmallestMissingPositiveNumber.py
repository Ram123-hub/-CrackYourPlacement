# You are given an array arr[] of N integers. The task is to find the smallest positive number missing from the array.

# Note: Positive number starts from 1.

# Example 1:

# Input:
# N = 5
# arr[] = {1,2,3,4,5}
# Output: 6
# Explanation: Smallest positive missing 
# number is 6.
# Example 2:

# Input:
# N = 5
# arr[] = {0,-10,1,3,-20}
# Output: 2
# Explanation: Smallest positive missing 
# number is 2.
# Your Task:
# The task is to complete the function missingNumber() which returns the smallest positive missing number in the array.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 <= N <= 106
# -106 <= arr[i] <= 106

def find_smallest_missing_positive(arr):
    positive_numbers = set()  # Initialize an empty set
    for x in arr:
        if x > 0:
            positive_numbers.add(x)  # Add positive numbers to the set

    smallest_missing = 1  # Start checking from 1
    
    while smallest_missing in positive_numbers:
        smallest_missing += 1
    
    return smallest_missing

# Example usage
N = 5
arr = [0, -10, 1, 3, -20]
print(find_smallest_missing_positive(arr))
