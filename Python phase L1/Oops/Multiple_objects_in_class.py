#class with multiple objects
class Cars():
    def Mahindra(self,model):
        print("Best car brand in India")
        print(model)
    def Tata(self,variant):
        print("Best safety car brand in India")
        print(variant)
# object is an instance of a class
obj1=Cars()   #object 1
obj1.Mahindra("BIG DADY scorpio N")
obj1.Tata("TATA punch")

obj2=Cars() #object 2
obj2.Mahindra("XUV 700")
obj2.Tata("Nexon")

