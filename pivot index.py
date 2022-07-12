# nums = [2, 1, -1]
# # case 1: If the first element is the pivot.
#
# pivot = nums[0]
# sumR = 0
# for i in range(1, len(nums)):
#     sumL = 0
#     sumR += nums[i]
#
# print(sumL)
# print(sumR)
# index = nums.index(pivot)
# if sumL == sumR:
#     print(index)
# elif sumL != sumR:
#     print("-1")
# else:
#     print(0)

# Case 2:
# num = [1,7,3,6,5,6]
#
# sumLeft = 0
# sumRight = 0
#
# for i in range(len(num)):
#     pivot_new = num[i + 1]
#     j = num.index(pivot_new)
#     sumRight = num[j+1:]
#     sumLeft = num[:j]
#     lsum = sum(sumLeft)
#     rsum = sum(sumRight)
#     if lsum == rsum:
#         print(j)
#         break
#     elif lsum != rsum:
#         print(-1)
#
#     else:
#         print(0)


def pivotIndex(nums):
    total_sum = sum(nums)
    leftSum = 0

    for i in range(len(nums)):
        pivot = nums[i]
        rightSum = total_sum - pivot - leftSum
        if leftSum == rightSum:
            return i
        leftSum += pivot

    return -1

print(pivotIndex([2, 1, -1]))


