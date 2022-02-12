# use union
set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)
# intersection_update
set1 = {"apple","pineapple","mango"}
set2 = {"microsoft","google","apple"}

set1.intersection_update(set2)
print(set1)

set1 = {"apple","pineapple","mango"}
set2 = {"microsoft","google","apple"}
set1.symmetric_difference_update(set2)
print(set1)

set1 = {"apple","pineapple","mango"}
set2 = {"microsoft","google","apple"}
z = set1.symmetric_difference(set2)
print(z)