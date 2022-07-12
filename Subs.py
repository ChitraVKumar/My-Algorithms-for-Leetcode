def Subs(s, t):
    a = ""
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    j = 0
    for i in range(len(t)):
        if t[i] == s[j]:
            a = a + t[i]
            if a == s:
                return True
            j += 1
    return False

print(Subs("knr", "karan"))

