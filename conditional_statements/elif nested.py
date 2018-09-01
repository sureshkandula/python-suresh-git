#!/usr/bin/python

char=input("Please enter any charcter : ")

if ord(char)>30 and ord(char)<60:
    print('character is in good shape')
    if ord(char) in ['a','e','i','o','u']:
        print('char is a vowel')
    else:
        print('character is a consonant')
elif ord(char)>=97 and ord(char)<=122:
    print ("You entered a lower case alphabet.", char)
    if char in ['a','e','i','o','u']:
        print ("You entered a vowel.", char)
    else:
        print ("You entered a consonant.", char)
else:
        print ("You did not enter an alphabet.", char)
print ("We are out of the if..elif block")