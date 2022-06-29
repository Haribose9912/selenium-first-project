# dictionary has key and value pair data

dic={"ID":45,"name":"hariesh","marks":99}
dic2={"ID":46,"name":"sharanya","marks":100}


print(dic)
print(dic2)
for i in dic:
    print(i)



# access items from dic
mydic={
    "brand":"tata",
    "model":"tata safari",
    "price":500000

}
print(mydic)
# access value from dic by passing key
print(mydic["model"])
# access value from dic by passing key

x=mydic.get("brand")
print(x)
# changing value in dic
mydic={
    "brand":"tata",
    "model":"tata safari",
    "price":500000

}
mydic["brand"]="mahindra"
mydic["model"]="big dady of SUVs"
print(mydic)

mydic={
    "Brand:":"tata",
    "Model:":"tata safari",
    "Price:":500000
}
# priting only keys using loop
print("priting only keys using loop")
for i in mydic:
    print(i)
# printing only values using loop
print("printing only values using loop")
for i in mydic:
    print(mydic[i])
# printing keys and  values using loop
print(" printing keys and  values using loop")
for x,y in mydic.items():
    print(x,y)

