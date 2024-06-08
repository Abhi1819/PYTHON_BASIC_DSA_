def create_file(filename):
	file = f'{filename}.py'
	with open(file,'w') as f:
		f.write(f'#{filename}')
		f.close()


create_file('Dictionary from Two Lists')