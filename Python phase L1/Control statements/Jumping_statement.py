#break and continue
print("break program")
for i in range(1,10):
    if i==5: # here it will give from 1 to 4 then from 5 it will not execute
        break
    print(i)

print("continue program")
for k in range(1, 10):
    if k == 5: # here in continue it will remove 5 number then gives remaining numbers
        continue
    print(k)

print("multiple continue program")

for i in range(1,10):
    if i==3 or i==5 or i==7: # here in continue it will remove 3 , 5 and 7 numbers then gives remaining numbers
        continue
    print(i)
print("done!!!")
