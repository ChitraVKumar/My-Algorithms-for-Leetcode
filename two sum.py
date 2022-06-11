nums = [2,7,5,4]
target = 9
# for i in range(0, len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i]+nums[j]==target:
#             print([i, j])
#
dictn = dict()

for i in range(len(nums)):
    num = nums[i]
    j = target - num

    if num in dictn:
       print([dictn[num], i])

    else:
        dictn[j] = i