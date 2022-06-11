
n = 6
for j in range(n):
    for i in range(j, n-1):
        print(" ", end="")
    for i in range(j+1):
        print("#", end="")
    print()