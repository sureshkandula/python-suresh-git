
string='my name is surESH kandula venkata'
print (len(string))
a='a'
""
print('count of a in the name:', string.count(a))
print('count of alphabets in a name:', string.count(a, 10, 20))
""
""""
print('strip method')
print('here is the strip for the string:', string.strip())
print('here is the rstrip for the string:', string.rstrip('venkata'))
print('here is the lstrip for the string:', string.lstrip('my name'))
"""
"""
print ('starts with :', string.startswith('my'))
print('ends with :', string.endswith('venkata'))
print ('starts with :', string.startswith('1my'))
print('ends with :', string.endswith('venkataa'))
"""
'''
print('ljust rjust:', string.rjust(40, '*'))
print('ljust ljust:', string.ljust(40, '*'))
'''
'''
str = "Python0007"
print(len(str))
print (str.rjust(20, '*'))
print (str.ljust(25, '#'))
'''

#print('centre of the string:', string.center(45,'a'))
print('centre of the string:', max(string))

van = "ekjfdfkjdfklsd"
print ("Min character: ",min(van))
print ("Max character: ",max(van))

van = "98509385698"

print ("Min character: ",min(van))
print ("Max character: ",max(van))


van = "9850938#5698"
print(string.title())
print(string.swapcase())

print(string.lower())
print(string.upper())
print(van.isdigit())
print(van.isdecimal())

print(van.isnumeric())
print(van.isalnum())