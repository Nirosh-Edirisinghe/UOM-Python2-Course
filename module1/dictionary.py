# create dictionary
my_dict = {}
print(type(my_dict))

nirosh = {
  "name":"niro",
  "age" : 25,
  "address" : "Kurunegala"
}

print(nirosh)
print(type(nirosh))


# dict() methos for create dictionary
my_dict1 = dict()
print(type(my_dict1)) 

sample_dict = dict([('name','niros'),('age',25)])
print(sample_dict)
print(type(sample_dict))


# access the element in dictionary
print(sample_dict['name'])
print(sample_dict.get('name'))


# add valaue to dictionary
sample_dict['address'] = "kurunegela"
print(sample_dict)


# update existing value 
sample_dict['age'] = 30
print(sample_dict)


# add and update dictionary using update key word
sample_dict.update({'address':'kurungela'})
print(sample_dict)

sample_dict.update(address = 'dodamgaslanda')
print(sample_dict)

# remove element
sample_dict.pop('address')
print(sample_dict)

# clear all
sample_dict.clear()
print(sample_dict)

# get all keys
list_item = list(sample_dict.keys())
print(list_item)

# iterate thorough dictionary
for key in sample_dict:
  print(key, sample_dict[key])

# example practice
names = ['amila', 'kamal', 'sunil', 'nimal', 'sunil', 'kamal', 'sunil', 'amila', 'nimal', 'sunil', 'kamal']
count = dict()

for name in names:
  if name not in count:
    count[name] = 1
  else:
    count[name] = count[name] + 1

print(count)