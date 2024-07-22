# Ceiling in a sorted array
# Last Updated : 10 Feb, 2023
# Given a sorted array and a value x, the ceiling of x is the smallest element in an array greater than or equal to x, and the floor is the greatest element smaller than or equal to x. Assume that the array is sorted in non-decreasing order. Write efficient functions to find the floor and ceiling of x. 
# Examples : 

# For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
# For x = 0:    floor doesn't exist in array,  ceil  = 1
# For x = 1:    floor  = 1,  ceil  = 1
# For x = 5:    floor  = 2,  ceil  = 8
# For x = 20:   floor  = 19,  ceil doesn't exist in array

def find_floor(arr,x):
    low , high = 0 , len(arr)-1
    floor_val = None

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] <x:
            floor_val = arr[mid]
            low = mid+1
        else:
            high = mid-1
    return floor_val

def find_ceiling(arr,x):
    low , high = 0 , len(arr)-1
    ceil_val = None

    while low<= high:
        mid = (low+high)//2

        if arr[mid] == x:
            return arr[mid]
        elif arr[mid]<x:
            low = mid+1
        else:
            ceil_val = arr[mid]
            high = mid-1
    return ceil_val

arr = [1, 2, 8, 10, 10, 12, 19]

x = 0
print(f"For x = {x}: floor = {find_floor(arr, x)}, ceil = {find_ceiling(arr, x)}") 

x = 1
print(f"For x = {x}: floor = {find_floor(arr, x)}, ceil = {find_ceiling(arr, x)}")  

x = 5
print(f"For x = {x}: floor = {find_floor(arr, x)}, ceil = {find_ceiling(arr, x)}") 

x = 20
print(f"For x = {x}: floor = {find_floor(arr, x)}, ceil = {find_ceiling(arr, x)}")  
