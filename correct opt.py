row, col = map(int, input().split())

for i in range(row // 2):
    print((".|."*((i * 2)+1)).center(col, "-"))

print("WELCOME".center(col, "-"))

for i in range(row // 2, -1, -1):
    print((".|."*((i * 2)+1)).center(col, "-"))