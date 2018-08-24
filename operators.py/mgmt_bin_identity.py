K="HEY SURESH"
V="YES HOWZ IT GOING"
S="HEY SURESH"

print(K in S)
print(K not in S)
print(K in V)

print('IDENTITY METHOD')
print(K is S)
print(V is not S)
print(K is V)

print('BINARY')
a=10
b=20
c=0
print('a:',a,':' ,bin(a), 'b=','b',':', bin(b))

c = a & b;
print ("result of AND is ", c,':',bin(c))

c = a | b;
print ("result of OR is ", c,':',bin(c))

c = a ^ b;        # 49 = 0011 0001
print ("result of EXOR is ", c,':',bin(c))

c = ~a;           # -61 = 1100 0011
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;       # 240 = 1111 0000
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;       # 15 = 0000 1111
print ("result of RIGHT SHIFT is ", c,':',bin(c))