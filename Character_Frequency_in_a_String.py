#Character_Frequency_in_a_String
def Char_freq(word:str):
   ds = {}
   for x in word:
     if x not in ds:
        ds[x]=1
     else:
        ds[x]+=1
   return ds


resp=Char_freq("Hello")
print(resp.items())
