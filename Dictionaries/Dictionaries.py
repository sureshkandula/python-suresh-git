'''
string={'a':"this is a dictionary file",'b':"i know that",'c':"ok boss"}
print(string['a'],string['b'],string['c'])

print(dict(string))
print(dict(enumerate(string)))

del string['c']

print(string)
'''

"""
suresh={'lastname':'kandula', 'middlename':'venkat'}
print('name of last name::{0} and his middle name::{1}' .format(suresh['lastname'],suresh['middlename']))
"""

dict1={'name':'suresh','age':37}

print("Equivalent String : %s" % str (dict1))

dict_2 = {'Name': 'minnu', 'Age': 7}
print ("Variable Type : %s" % str(dict_2))

dict_3 = {'Name': 'minnu', 'Age': 7};
print ("Start Len : %d" % len(dict_3))

dict={"FirstName":'Guido',"MiddleName":'Van',"LastName":'Rossum','Age':58}

print(dict)

print ("suresh end : %d" %  len(dict))

dict5=dict.copy()
print('new dictionary:', str(dict5))

student={'name':'alibaba','age':7,'std':'second'}
print ("Value : %s" % student.get('age'))
print('value of age:', student.get('age'))
print('value of age:', student.get(7))
print ("Value : %d" %  student.get('Education', 1))

print ("Calling All Keys : ",dict.keys())
print ("Calling All Values : ",dict.values())
student['age']=7
print(student)
