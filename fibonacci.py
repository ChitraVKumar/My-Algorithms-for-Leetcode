nums = 1
a = 0
b = 1
c = 0


# for i in range(2, nums+1):
#     c = a + b
#     a = b
#     b = c
# print(c)
i = 2
if nums == 1:
    print(1)
while i < nums+1:
    c = a + b
    a = b
    b = c
    i += 1
print(c)


