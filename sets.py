x=set([1,2,3,4])
y=set([5,6,7,8])

print (set([1, 2, 3, 4, 5]).union(set([2,5,6, 7])))        #diplay all the values
print (set([3,4,5,5]).intersection(set([2,4,5,6])))       #display only common set a nd set b
print (set([3,4,5,5,6,9]).difference(set([8,9,5,6])))     #display only set A  values which are not in set B
print(set([3,5,6,7,9]).symmetric_difference([4,5,6,8]))   #displays all unique values from both the sets
print (set([3,4,5,6]).issubset([3,4,6,5]))               # set a all values in set b --true
print (set([3,4,5,6]).issuperset([5]))                    # set B compares with set A
print(set([4,5,6,7,8,9]).union(set([11,12,3,13,10])))