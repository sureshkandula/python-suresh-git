
string=['here we go today is thursday and no school for shruthika']
print(string)
string.append(' yes it is !!')
print(string)

print("modifying the string for extend method:")

string=[1,2,3,4]
string1=[5,6,7,8]
print(string)
string.extend(string1)
print(string)

print("modifying the string for insert method:")

string2=['hello mr suresh']
string2.insert(0,'babu')
print(string2)
string3=['venkat']
string3.insert(0,'kandula')
print(string3)

print("modifying the string for remove method:")

string4=['this is to remove of the remove ','remove']
string4.remove('remove')
print(string4)

print("modifying the string for POP method:")

string5=['i love you gunnu', 'fellowlu']
print(string5)
string5.pop()
print(string5)
string6=['i love you gunnu', 'fellowlu','jhonson']
print(string6)
string6.pop(2)
print(string6)

print("modifying the string for REVERSE method:")
string7=['vintunnava','suresh','venkata','kandula', 'myname is']
print(string7)
string7.reverse()
print(string7)

print("modifying the string for SORT method:")
string8=['vintunnava','suresh','venkata','kandula', 'myname is']
string8.sort()
print(string8)

print("modifying the string for INDEX method:")
string9=['vintunnava','suresh','venkata','kandula', 'myname is']
print(string9.index('suresh'))

print("modifying the string for COUNT method:")
string10=['vintunnava','suresh','venkata','kandula', 'kandula', 'kandula', 'myname is']
print(string10.count('kandula'))