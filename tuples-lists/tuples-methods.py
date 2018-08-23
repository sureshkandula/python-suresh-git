
tup=('hello he-man how are you doing', 'i am fine','thank you')
tup1=(1,2,3,4)
tup2=('''a''','''b''','''c''')
tup3=("a","b","c","d")

print(tup,type(tup),len(tup),id(tup))
print(tup1,type(tup1),len(tup1),id(tup1))
print(tup2,type(tup2),len(tup2),id(tup2))
print(tup3,type(tup3),len(tup3),id(tup3))

print(tup3[2])
print(tup2[1])
print(tup1[0])
print(tup[0])

print('this is to show tuple list')
string=(1,2,3,4,"alphabet")
string2=tuple(string)
print(string2)
print ("Tuple elements : ",type(string2),string2)

print("Convert tuple into list",list(string2),type(string2))

print('this is to show ACCESSING tuple list')

tupsure=(1,2,3,5)
tupsiri=('a','b','c','d')
print('min value:', min(tupsure))
print('max value', max(tupsiri))
