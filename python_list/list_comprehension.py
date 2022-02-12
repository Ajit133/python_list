fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = [x for x in fruits if "a" in x]

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
personname = ["Ajit","Roni","Sajib","Gurab","koli","rajib","sonju"]
person1 = [i for i in personname if "a" in i]
print(person1)
fruits = ["apple","cherry","banana","kiwi","mango"] 
newfruits = [ x for x in fruits if x != "apple"]
print(newfruits)
newlist = [x for x in range(10)]
print(newlist)
fruits.sort()
print(fruits)
number = [50,30,20,19,40,37,390,67,30,69,56,65]
number.sort(reverse=True)
print(number)
# sort descending
# if you can want to create your own function you can do this function
# Example



