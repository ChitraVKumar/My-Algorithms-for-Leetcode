def isPhoneNumber(Number):
    if len(Number) != 12:
        return False

    for num in range(0, 3):
        # print(Number[num])
        if not Number[num].isdecimal():
            return False
    if Number[3] != "-":
        return False
    # else:
        # print("-")

    for num in range(4, 7):
        # print(Number[num])
        if not Number[num].isdecimal():
            return False
    if Number[7] != "-":
        return False
    # else:
        # print("-")
    for num in range(8, 12):
        # print(Number[num])
        if not Number[num].isdecimal():
            return False
    return Number


# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
print("Done")