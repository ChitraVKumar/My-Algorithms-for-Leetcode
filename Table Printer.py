tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

print(len(tableData))
n = len(tableData)
# for x in range(n+1):
#     for j in range(n):
#         print(tableData[j][x], end=" ")
#     print()

max_count = 0
new_list = []
for list in tableData:
    for ele in list:
        if len(ele) > max_count:
            tableData.insert(0, ele)
            max_count = len(ele)
        else:
            tableData.append(ele)
print(tableData)