# a = [1,2,3,4,4,3,2,1]

# n = len(a)
# b = int(n/2)
# x = a[0:b]
# print(x)
# y = a[b:]
# new_arr = []
#
# for i in range(0, len(x)):
#     new_arr.append(x[i])
#     new_arr.append(y[i])
# print(new_arr)

nums = [1,2,3,4,4,3,2,1]
n = 4

r = [0] * (n * 2)
for i in range(n):
    r[i * 2] = nums[i]
    r[i * 2 + 1] = nums[i + n]

print(r)
