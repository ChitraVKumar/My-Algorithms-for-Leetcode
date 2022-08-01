arr = [1, 2, 3, 4, 5, 6]

temp = 0
for i in range(0, len(arr)//2):
    temp = arr[i]
    arr[i] = arr[len(arr)-1-i]
    arr[len(arr) - 1-i] = temp

print(arr)
print(len(arr))