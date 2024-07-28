def minSwapsToSort(nums):
    sorted_nums = sorted(nums)

    index_map = {}
    for idx, value in enumerate(sorted_nums):
        index_map[value] = idx
    
    visited = [False]*len(nums)

    def count_cycle_lengths(start_idx):
        length = 0 
        current_index = start_idx
        while not visited[current_index]:
            visited[current_index] = True
            next_idx = index_map[nums[current_index]]
            current_index = next_idx
            length += 1
        return length
    
    min_swaps = 0 
    for i in range(len(nums)):
        if not visited[i]:
            cycle_lengths = count_cycle_lengths(i)
            if cycle_lengths > 1:
                min_swaps += cycle_lengths-1
    return min_swaps

nums = [2,8,5,4]
print(minSwapsToSort(nums))


