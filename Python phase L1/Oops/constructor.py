class test():
    def __init__(self):
        print("called constructor...")
        # print(num)
    def  motor(self):
        print("Hero motocop")

    def cars(self,x,y):
        return (x+y)

t=test()
t.motor()
res=t.cars(12,3)   # res from tuples
print(res)


# parameterised constructor
class Building():
    def __init__(self,steel,cement,sand): #local variables
         # converting local variables to class variables
         self.steel=steel #class variables
         self.cement=cement #class variables
         self.sand=sand #class variables

    def display(self):
        print(self.steel,self.sand,self.cement)
kt=Building(10,950,20) #object 1
kt.display()

kt2=Building(16,88,98) #object 2
kt2.display()
