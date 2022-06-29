a=int(input("Enter 1st global number: ")) #global variables
b=int(input("Enter 2nd global number: ")) #global variables
# a=10
# b=20
class calc():
    x=input("Enter your name: ")
    y=input("Enter your Father name: ")

    def add(self):
        print(a+b) #accessing global variables
    def Family(self):
        print("Hello "+self.x) #accessing class variables
        print("Thanks "+self.y) #accessing class variables
    def cars(self,p,q): #local variables
        print(p+q)
test=calc()
test.add()
test.Family()
test.cars(10,20)
