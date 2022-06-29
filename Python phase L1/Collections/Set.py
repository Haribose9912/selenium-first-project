# set is mutable hence can make all the changes like list
myset={"hariersh","sharanya","sun","moon"}
print(myset)

# accessing items from set can be done by only loop
myset={"hariersh","sharanya","sun","moon"}
for i in myset:
    print(i)

# find items present in set or not

print("sun" in myset)
print("run" in myset)
print("moon" in myset)

# add() and update() for adding single item need add() and for adding multiple items need update() the set
myset={"hariersh","sharanya","sun","moon"}
# add
myset.add("mercury")
print(myset)
# update
myset.update(["mars","saturn"])
print(myset)

# removing the item remove() and discard()
myset={"hariersh","sharanya","sun","moon","mars"}
print(myset)
myset.remove("mars")
print(myset)

# clear
myset.clear()
print(myset)

# joining two sets using union() function
myset1={"hariersh","sharanya","sun","moon","mars"}
myset2={"sat","mon","thurs","tues"}
myset3=myset1.union(myset2)
print(myset3)
# joining two sets using update() function
myset1={"hariersh","sharanya","sun","moon","mars"}
myset2={"sat","mon","thurs","tues"}
myset1.update(myset2)
print(myset1)






