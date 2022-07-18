# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] == nums[j]:
#             nums.append(nums[j])
#             nums.remove(nums[j])
#             print(nums)
#             j -= 1
#         else:
#             i = j
#             j += 1
# print(nums)
def removeDup(nums):
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1

    return l

print(removeDup([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))