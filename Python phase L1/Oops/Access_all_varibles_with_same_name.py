
# Here all local,global,class having same name variables but to access we have different ways.
a,b=20,30

class clac():
    a,b=15,20
    def add(self,a,b):
        print("This value from local variables")
        print(a+b)
        print("This value from class variables")
        print(self.a+self.b)
        print("This value from global variables")
        print(globals()['a']+globals()['b'])

H=clac()
H.add(88,20)