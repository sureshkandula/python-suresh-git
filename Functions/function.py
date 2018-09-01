"""
def function(mylist1):
    mylist1=([4,5,6])
    print('see here:', mylist1)
    return

mlist =([1,2,3])
function(mlist)
print('see;', mlist)
"""
"""
def mul(arg1,arg2):
    total= arg1*arg2
    print('see here arthimatic:', total)
    return total

mlist =mul(7,8)
print('see;', mlist)
"""
"""
def sum(arg1,arg2):
    total= arg1*arg2
    print('see here arthimatic:', total)
    return total

mlist =sum(7,8)
print('see;', mlist)
"""
"""
def centos(gunnu11):
    gunnu11.append([1,2,3,4])
    print('see here apendone:', gunnu11)
    return

mlist =[5,6,7,8]
centos(mlist)
print('see;', mlist)
"""
"""
def printme(name,age):
    print("name:", name)
    print("age:", age)
    return
printme(name='suresh',age = 39)
"""
"""
#default arguement
def printme(name,age=39):
    print("name:", name)
    print("age:", age)
    return
printme(name='suresh')
"""
"""
#variable arguement

def printname(name,*vartuple):
    print("output is:" )
    print(name)
    for var in vartuple:
        print (var)
    return
printname('suresh')
printname(1,2,3,3)
"""
"""
def printname(name,*vartuple):
    print("output is :{}" .format (name) )
#   print(name)
    for var in vartuple:
        print (var)
    return
printname('surik', 1,2,3,4,4,4,4)
"""
"""
#global variables

_global0,_global1=100,200
def multiply(numberone,numbertwo):
    abc=numberone*numbertwo
    print(abc)
    print(_global0)
    print(_global1)
    return
multiply(_global0,_global1)
"""

#practicing functions

def happy(a,b,c=8,):
    f=(a*b*c)
    print (f)
    return f
d=happy(3,4,9)
print ('display the total d:', d)


"""
def smile(a,b,*vartuple):
    step1=(a,b)
    print ("display step1 :", step1)
    for var in vartuple:
        print (var)
    return 
smile('suresh','sirisha','shruthika','neha','ravi','ashish')
"""