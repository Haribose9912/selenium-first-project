#ways of creating string variable
# all are same
s="welcome"
s='welcome'
s=str('welcome')
s=str("welcome")

# creation empty string
s=''
name=""
name=str()

# mutable cannot change value of variable any time
# immutable can change value of variable.
# string is immutable

str1="welcome"
print(id(str1)) # id() function used to print id of the string
print(str1)

str1=str1+" python"
print(id(str1))
print(str1)
# if the value has been changed after update then it is a immutable
# Hence string is immutable

#  '+' will used for concatination
str = "hari"
str1=str+"esh"
print(str1)
#  '*'  will used for printing multiple times
print(str1*5)

# slicing operator
str = "harish"
print(str[1:3])  #printing from strating and ending index

# ord()  chr()
print("ord() will give # key value of given letter")
print(ord('A'))
print("chr() this will give charecter of given value")
print(chr(65))
print("length of charecter")
print(len("hariesh"))

# in and not operator
print("program for in and not operator")
s="welcome"
print("wel" in s)
print("mkj" in s)

# testing string true or false

s="hariesh on python"
print(s.isalnum())
print(s.isdigit())
print(s.isdecimal())
print(s.isalpha())
print(s.isnumeric())
print(s.islower())
print(s.isidentifier())