nums = [1,1,1,1]
arr = []

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if i < j:
            if nums[i] == nums[j]:
                # result = print("(" + str(i) + "," + str(j) + ")")
                arr.append(tuple([i, j]))
                j += 1
print(len(arr))