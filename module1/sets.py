# create set 

my_set = {"nirosh","prasanna",10}
print(my_set)

my_set1 = set(["nirosh","prasanna",10])
print(my_set1)

# length of set
length = len(my_set)
print(length)

# access item in set
for item in my_set:
  print(item)


# add single elmemnt
my_set.add("edirisinghe")
print(my_set)

# add myltiple element
my_set.update(["hellow","world"])
print(my_set)

# remove elemenet
my_set.remove("hellow")
print(my_set)

my_set.discard("world")
print(my_set)

my_set.pop()
print(my_set)


# Union of set
A = {1,2,3,4,5}
B = {3,4,5,6,7}

print(A|B)
print(A.union(B))

# Intersection of set
print(A & B)
print(A.intersection(B))

# set difference
print(A - B)
print(A.difference(B))