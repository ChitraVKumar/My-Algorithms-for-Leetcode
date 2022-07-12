# Algorithm:
# 1. Create empty dictionaries for mapping of string1 --> string2 and string2 --> string1
# 2. A for loop in the range of length of string and an index i to track the index of both the strings.
# 3. Create two variable to track characters from both strings
# 4. if condition returns FALSE if:
#       1. Two conditions using AND: char1 is in dictST and the value of dictST[char1] != char2 (both conditions should be True to execute)
#                                                   OR(either conditions should be true)
#       2. Two conditions using AND: char2 is in dictTS and the value of dictTS[char2] != char1 (both conditions should be True to execute)
# mapping dictST[char1] = char2
# mapping

def isomorphic(s, t):
    dictST = {}
    dictTS = {}

    for i in range(len(s)):
        char1 = s[i]
        char2 = t[i]

        if (char1 in dictST and dictST[char1] != char2) or (char2 in dictTS and dictTS[char2] != char1):
            return False

        dictST[char1] = char2
        dictTS[char2] = char1

    return True


print(isomorphic('egg', 'foo'))
