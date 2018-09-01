"""
count=0
name=input('enter name:')
for letter in name:
    if (letter in ['a','i','o','e','u']):
        count=count+1
print('you have', count, 'value in the vowels')
"""
""""
var=1
while (var<=15):
    if (var==10):
        break
    print(var)
    var=var+1
print("we are out of the while loop")
"""
"""
while True:
    print("enter an intezer")
    num=input()
    if(ord(num) in range(59,69)):
        break
print("we are done and ready to shutdown")
"""

def function(mylist1):
    mylist1=([4,5,6])
    print('see here:', mylist1)
    return

mlist =([1,2,3])
function(mlist)
print('see;', mlist)

