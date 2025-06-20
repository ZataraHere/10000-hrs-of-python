def search_insert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


