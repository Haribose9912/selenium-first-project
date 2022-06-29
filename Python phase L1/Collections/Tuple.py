#in tuple cannot modify,insert,remove the items
# But it can be done by coverting tuple into list
# remaining all functions are same like list (join,del,copy)

mytuple=("hariersh","sharanya","sun","moon")
print(mytuple)
mylist=list(mytuple) # coverting to "List"
print(mylist)
mylist[2]="mars" # changing item
print(mylist)
mytuple=tuple(mylist) #coverting to "Tuple"
print(mytuple)
# comparing two tuples
print("comparing two tuples")
mytup1=("hariersh","sharanya","sun","moon")
mytup2=("hello","python")
if mytup1==mytup2:
    print("both are same")
else:
    print("Both are not same")