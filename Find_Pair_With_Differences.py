def find_pair_with_difference(arr, n, x):
    elements = set()

    for num in arr:
        if (num+x) in elements or (num-x) in elements:
            return 1
        elements.add(num)
    return -1

arr = [5, 20, 3, 2, 5, 80]
n = 6
x = 78

result = find_pair_with_difference(arr, n, x)
print(result)  