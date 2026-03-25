# create tuple
tuple_1 = ('a', 'b', 20, 14.5)
print(type(tuple_1))

tuple_2 = ('a')
print(type(tuple_2))

tuple_3 = ('a',)
print(type(tuple_3))


# access value in tuple
my_tuple = (1,2,3,4,5,6)
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[-1])


# slicing
print(my_tuple[0:3])

# nested tupel
my_tuple1 = ((1, 2), ('a', 'b', 1))
print(my_tuple1[0][1])
print(my_tuple1[1])

# tuple packing and tuple unpacking
my_car = ('benz', 'bmw', 'audi')
print(my_car)

Benz,Bmw,Audi = my_car
print(Benz)
print(Bmw)
print(Audi)

my_num = (1,2,3)
my_num2 = (4,5,6)
print(len(my_num))
print(my_num + my_num2)