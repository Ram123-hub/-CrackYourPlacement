def can_permute_arrays(arr1, arr2,k):
    arr1.sort()
    arr2.sort(reverse=True)

    for a , b in zip(arr1, arr2):
        if a+b <k:
            return False
    return True


arr1 = [2,1,3]
arr2 = [7,8,9]
k =10


if can_permute_arrays(arr1, arr2, k):
     print("Yes, it's possible to permute the arrays to meet the condition.")
else:
    print("No, it's not possible to permute the arrays to meet the condition.")
    