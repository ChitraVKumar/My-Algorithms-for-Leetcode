import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search("My number is 415-555-4242.")
print("Phone Number found: " + matchObject.group())

heroRegex = re.compile(r'Batman|Tina Frey')
mo1 = heroRegex.search("Batman and Tina Frey.")
print("The first occurrence is: " + mo1.group())
mo2 = heroRegex.search("Tina Frey and the Batman.")
print("The first occurrence is: " + mo2.group())

batRegex = re.compile(r'Bat(man|Mobile|Copter|Bat)')
mo3 = batRegex.search("BatMobile lost a wheel")
print(mo3.group())
print(mo3.group(1))

regex = re.compile(r'Bat(wo)?man')
mo4 = regex.search("The adventures of Batman.")
print(mo4.group())
mo5 = regex.search("The adventures of Batwoman.")
print(mo5.group())

phoneRegex = re.compile(r'(\d\d\d)?-(\d\d\d-\d\d\d\d)')
mo6 = phoneRegex.search('My number is 415-555-4242')
print(mo6.group())
mo7 = phoneRegex.search('My number is 4-555-4242')
print(mo7.group())

# Matching zero or more with *
batRegex = re.compile(r'Bat(wo)*man')
mo8 = batRegex.search("The Adventures of Batwowowowowomanwomanwoman")
print(mo8.group())

# Matching One or More with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo9 = batRegex.search("The adventures of Batwoman")
print(mo9.group())
