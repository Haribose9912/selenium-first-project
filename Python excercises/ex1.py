#Exercise 1: Calculate the multiplication and sum of two numbers

# given
def mul_or_sum(num1,num2): #this is a method
    # calculate multiply of two numbers

    multi = num1 * num2
    # check if the product is less than 1000
    if multi <= 1000:
        return multi
    else:
        # calculate sum of two numbers
        return num1 + num2
# condition-1
result=mul_or_sum(20,30)
print("The result is : ",result)
# condition-2
result=mul_or_sum(50,90)
print("The result is : ",result)




