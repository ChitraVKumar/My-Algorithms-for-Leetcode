# Algorithm
# 1. Initialize an empty string res
# 2. Use for loop to loop through the first string strs[0], with a pointer i indication index of first string.
# 3. Use another for loop to loop through the each remaining strings s in the list strs.
# 4. if the index i == to the length of the other string in strs(to check out of bounds case) OR if the string s[i] != strs[0][i](one by one checking
# if each letter in string s of list strs and the letter of first string in strs is equal or not).
#   5. then return the string res.
# 6. Append the initialized string res with the letter of first string of list strs[0][i].
# 7. return the result.

def longest_comm_prefix(strs):

    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            l = len(s)
            if i == l or s[i] != strs[0][i]:
                return res
        res += strs[0][i]

    return res

print(longest_comm_prefix(["flower", "flow", "flight"]))
