candies = [2,3,5,1,3]
extraCandies = 3

new_cand = []

maxi = max(candies)
print(maxi)

for i in range(len(candies)):
    if candies[i] + extraCandies >= maxi:
        new_cand.append(True)

    else:
        new_cand.append(False)

print(new_cand)