
def removeDuplicates(self, nums):
    if not nums:  # Handle empty list case
        return 0
        
    j = 0  
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1 
            nums[j] = nums[i] 

    return j + 1  