def recursive_sum(array, idx=0):
    if idx == len(array) - 1:
        return array[idx]
    return array[idx] + recursive_sum(array, idx+1)

nums = [1, 2, 3, 4]

print(recursive_sum(nums))