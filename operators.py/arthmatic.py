a=2
b=4
"""
print('a+b=', a+b)
print('a-b=', a-b)
print('a*b=', a*b)
print('a/b=', a/b)
print('a**b=', a**b)
print('a//b=', a//b)
"""
"""
print ('LOGICAL:')

x=False
y=True
print('x and y=:', x and y )
print('x or y=:', x or y )
print ('x not y=', y | x)
print('x ^ y=:', x ^ y )
"""

print ('RELATIONAL')

a=8
b=8
c=10
print(a==b)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a!=b)

a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", id(a),id(b),id(c),type(c),c)

print(c)
c += a
print ("Line 2 - Value of c is ", id(a),id(b),id(c),type(c),"c + a", c , sep=':')

print(c)

