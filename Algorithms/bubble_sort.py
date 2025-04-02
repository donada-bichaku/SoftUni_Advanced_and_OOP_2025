def bubble_sort(nums):
    is_sorted = False
    i = 0
    while not is_sorted:
        is_sorted = True
        for j in range(0, len(nums) - i - 1):
            if nums[j+1] < nums[j]:
                nums[j + 1], nums[j] = nums[j], nums[j+1]
                is_sorted = False

        i += 1

nums = [int(x) for x in input().split()]
bubble_sort(nums)
print(*nums)
