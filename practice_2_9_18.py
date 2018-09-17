#practice the commands till now

k='hello world'
print (k)

name='suresh venkata babu kandula'
name1='bandaru'
age=38
profession='associate'
print('display what i have written :', name,age,profession,len(name),type(age),id(profession))

print('Name :{}'.format ('KANDULA VENTAT SURESH BABU'))

'''
print('count of s in the string name:', name.count('s'))
print('index:', name.index(name1))
'''
'''
str1 = "this is string example....wow wow second wow!!!"
str2 = "wow"
print (str1.rindex(str2))
print (str1.index(str2))

print (str1.find(str2))
print (str1.rfind(str2))
'''
'''
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 30))

str = "Python0007"

print(len(str))

print (str.rjust(20, '*'))

print (str.ljust(25, '#'))
'''
str1 = "this is string example....wow wow second wow!!!"
str2= "123"
print(str1.replace('string', 'shouting'))
print(str1)

print(str1.capitalize())
print(str1.join(str2))

s = "  &  "
seq = ("a", "b", "c") # This is sequence of strings.

print (s.join(seq))

alph_lower = "abcdefghiJKlmnopqrstuvwxyz"

print (alph_lower.swapcase())

print (alph_lower.upper())