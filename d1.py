# cars={
# 	'color':'blue',
# 	'brand':'Ferrari',
# 	'price':'10CR',
# 	'brand':'tesla'
# }

# # print(cars['brand'])

# # so the values in case of dict - duplicates are not allowed.. if did newer values are only considered

# # print keys

# # print(cars.keys())

# # a =cars.get("brand")
# # print(a)
# # cars['rating']='5 Star'

# # print(cars.items())


# #  check for specific keys

# # if "tesla" in cars:
# 	# print("True")

# # update method() - it must be a dir or key value iterable

# cars.update({'max_speed':'400kmh'})
# print(cars.items())

# # del cars['max_speed']
# # print(cars.items())

# # cars.popitem()
# # print(cars.items())

# # cars.pop('color')
# # print(cars.items())

# # cars.clear()
# # print(cars.items())

# # looping throught dict
# # 
# # for x,y in cars.items():
# 	# print(x,y)

# #  cant make copy directly like a = b ; i.e. it will only give ref to first one
# # changing first one will reflect to dict 2

# c = cars.copy()

# print((c.items()))

#  nested dicts

# family={
# 	"child1":{"name":'x',"age":43},
# 	"child2":{"name":"y","age":32}
# }

# print(family.items())

child1 = {
    "name": "Alice",
    "age": 6,
    "grade": "1st",
    "hobbies": ["painting", "cycling"],
    'relation':'sister'
}

child2 = {
    "name": "Bob",
    "age": 8,
    "grade": "3rd",
    "hobbies": ["reading", "soccer"],
    "relation":'brother'
}

fam = {
    "first_child": child1,
    "second_child": child2
}

fam.setdefault('relative','True')


if 