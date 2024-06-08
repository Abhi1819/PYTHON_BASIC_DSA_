l = [1,3,4,2,5,2,35,23,2,1]
d= {}
duplicate= False
for x in l:
	if x in d:
		duplicate=True
		break
	d[x]=''

print(d.items())
if duplicate:
	print('it contains duplicate')
else:
	print("'doesn't contain duplicate")