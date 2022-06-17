nums = [1, 2, 1]
# ans = []
#
# for i in range(len(nums)):
#     ans.append(nums[nums[i]])
#
# print(ans)



n = len(nums)
ans = nums + nums
for i in range(n):
    ans[i] = nums[i]
    ans[i+n] = nums[i]

# for i in range(len(nums)):
#     ans.append(nums[i])
#
# for i in range(len(nums)):
#     ans.append(nums[i])



print(ans)
