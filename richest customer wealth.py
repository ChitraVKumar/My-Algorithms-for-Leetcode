acc = [[1,2,3],[3,2,1]]

max_wealth = 0

for i in range(len(acc)):
    total_sum = sum(acc[i])
    max_wealth = max(max_wealth, total_sum)

print(max_wealth)