def find_peak_element(nums):
    low , high = 0 , len(nums)-1

    while low < high:
        mid = (low+high)//2

        if nums[mid] > nums[mid+1]:
            high = mid
        else:
            low = mid+1
    return low

arr1 = [1, 2, 3, 1]
print(find_peak_element(arr1))  

arr2 = [1, 2, 1, 3, 5, 6, 4]
print(find_peak_element(arr2))  