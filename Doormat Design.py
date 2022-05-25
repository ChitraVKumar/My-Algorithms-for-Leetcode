num = 5

# for i in range(num, 0, -1):
#     for j in range(0, i):
#         print("*", end=" ")
#     print()


row = 7
col = 21
for i in range(0, row+1, 2):
    for j in range(0, col+1):
        print(".|.", end=" ")
    print()