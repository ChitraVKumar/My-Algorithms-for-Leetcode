def removEle(nums, val):
    l = 0
    for r in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
    print(nums)
    return l

print(removEle([3, 2, 2, 3], 3))
