thisset = {"mango","apple","banana"}
thisset.add("orange")
print(thisset)

# update set
thisset = {"mango","apple","banana"}
tropical = {"pineapple","cucamber","cherry"}
thisset.update(tropical)
print(thisset)

# add any iterable 
thisset = {"mango","apple","banana"}
newset = ["jackfruit","orange"]
thisset.update(newset)
print(thisset)