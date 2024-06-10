# group anagram.py

def ana(ls:list) -> list:
   ds={}
   for x in ls:
          s_word=''.join(sorted(x))
		if s_word not in ds:
			ds[x]=''
		else:
			ds[x]=x
   return ds


resp = ana(['tea', 'ate', 'king', 'gink', 'gemini'])
print(resp.items())


