# chnage the list items
from telnetlib import theNULL


li = ["apple","banana","jackfood","orange","pineapple","cherry"]
li [1:3] = "balckcurrent","watermelon"
print(li)
# Change the second value by replacing it with two new values:
thislist = ["apple","Banana","Cherry"]
thislist[1:2] = ["blackcurrent","watermelon"]
print(thislist)
# insert items
thislist = ["apple","Banana","cherry"]
thislist.insert(2,"mango")
print(thislist)
# append items
thislist = ["apple","Banana","cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple","Banana","cherry"]
thislist.append("cucamber")
print(thislist)
# extend list
thislist = ["orange","mango","banana","jackfruit"]
fruits = ["orange","cucamber","cherry"]
thislist.extend(fruits)
print(thislist)
# Add elements of a tuple to a list:
thislist = ["orange","mango","banana","jackfruit"]
set1 = ("orange","cucamber","cherry")
thislist.extend(set1)
print(thislist)