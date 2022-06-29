class world:
    def India(self):   #instance method
        print("India is a Best country")
    def USA(self,name):
        print("USA is a Median country")
        print(name)

mc1=world() #mc1 is a variable and now world() is an object
mc1.India()  #Inida() is a object of world class
mc1.USA("Harish")

#static method

class universe:
    def Galaxy(self):
        print("Milkyway galaxy")
    @staticmethod
    def Planet(self,num):
        print("There are many planets in this entire galaxy")

K=universe()
K.Galaxy()
#ACCESSING STATIC METHOD

universe().Planet(20,100)