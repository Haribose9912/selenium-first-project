mylist =[10.20,1,4]
print(mylist)

list2=["apple",10,1.5,"kill"]
print(list2)

# empty list
list3=list()

# accessing items from the list

lis=["apple","hariesh","sharanya","shiva","vishnu","sun","moon"]
print(lis[1])
print(lis[2])
print(lis[-1]) # -1 prints last value
print(lis[2:5])
print(lis[-4:-1])

# change the item  values

lis[0]="mango"
print(lis[0])
print(lis)

# length of items in list
mylist=["hariersh","sharanya","sun","moon"]
print(len(mylist))

# add new item to the list using append() function or insert() function
mylist.append("parvathi")
print(mylist)
print("inserting an new item")
mylist.insert(0,"python") # should specify index to add item at particular index
print(mylist)

# remove item from list using pop() function
mylist=["hariersh","sharanya","sun","moon"]
mylist.pop(2)
print(mylist)
#  use del keyword to delete the item from list
mylist=["hariersh","sharanya","sun","moon"]
del mylist[2]
print(mylist)
# clear all items from the list
mylist=["hariersh","sharanya","sun","moon"]
mylist.clear()
print(mylist)


