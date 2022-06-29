#searching for sub string

s="hariesh kumar"
print(s.endswith("kumar"))
print(s.startswith("kumar"))
print(s.find("kumar"))
print(s.count("k"))

# convert the string

s="python is GOOD"
s1=s.capitalize()
print(s1)
s2=s.title()
print(s2)
s3=s.upper()
print(s3)

# replace string
s4=s.replace("is", "is too")
print(s4)

# Reversing a string

print("Reversing string")
s="python"
rev_str=""
for i in s:
    rev_str=i+rev_str
print("reverse string is : "+ rev_str)

# medthod 2 reverse string
print("medthod 2 reverse string")
s="hariesh"
revstr=s[::-1] #using slicing operator
print(revstr)