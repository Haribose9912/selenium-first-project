global_var="hello global"
# function()
def test():
    print("hello world")

test()
# function() using parameter
def test1(name):
    print("hello",name)

test1("the king")


# function() using return statement
def calc(a,b):
    return(a+b)
print(calc(10,20))

# global variable which is outside function

def lvar():
    local_var="hello local"
    print(local_var) # it can be accessed from inside the function only
    print(global_var)

lvar()
# print("Global variable: "+ global_var)
print(global_var) # global var can be accessed from any where