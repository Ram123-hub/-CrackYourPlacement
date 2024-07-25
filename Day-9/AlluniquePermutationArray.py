# Given an array arr[] of length n. Find all possible unique permutations of the array in sorted order. A sequence A is greater than sequence B if there is an index i for which Aj = Bj for all j<i and Ai > Bi.

# Example 1:

# Input: 
# n = 3
# arr[] = {1, 2, 1}
# Output: 
# 1 1 2
# 1 2 1
# 2 1 1
# Explanation:
# These are the only possible unique permutations
# for the given array.

def find_sorted_unique_permutations(arr):
    result = []
    arr.sort() # Sort the array to ensure lexicographical order
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
            return
        seen = set()

        for i in range(start, len(arr)):
            if arr[i] not in seen:
                seen.add(arr[i])
            # Swap elements to create new permutation
                arr[start] , arr[i] = arr[i] ,arr[start]
                backtrack(start+1)
                arr[start] , arr[i] = arr[i] ,arr[start]
    backtrack(0)
    return result

arr = [1, 2, 1]
n = len(arr)
result = find_sorted_unique_permutations(arr)


for perm in result:
    print(' '.join(map(str, perm)))

    







        

        