#Dictionary from Two Lists
l1 = ['ferrari','5Cr','black',500,'benz']
l2 = ['brand','price','color','price','brand']
car = {}
for x in range(len(l1)):
	car[l2[x]]=l1[x]

print(car.items())