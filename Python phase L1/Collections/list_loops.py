# print all values at once in form of list using looping statement
mylist=["hariersh","sharanya","sun","moon"]
print(mylist)
for i in mylist:
    print(i)

# search the items in the list using IF and else condition
mylist=["hariersh","sharanya","sun","moon"]
if "sun" in mylist:
    print("yes, this item present in list")
else:
    print("No, this item does not present in the list")


# copy from one list to other list
mylist=["hariersh","sharanya","sun","moon"]
mylist2=list(mylist)
print(mylist)
print(mylist2)

# copy from one list to other list using copy() function
mylist=["hariersh","sharanya","sun","moon"]
mylist2=mylist.copy()

print(mylist)
print(mylist2)

# combine or join 2 lists
mylist=["hariersh","sharanya","sun","moon"]
mylist2=["sun","mercury","moon","mars"]
list3=mylist+mylist2
print(list3)

# joining 2 lists using loop
print("joining 2 lists using loop")
mylist=["hariersh","sharanya","sun","moon"]
mylist2=["sun","mercury","moon","mars"]

for i in mylist2:
    mylist.append(i)
print(mylist)
