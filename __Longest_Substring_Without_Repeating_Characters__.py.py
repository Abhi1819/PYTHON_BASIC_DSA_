#__Longest_Substring_Without_Repeating_Characters__.py

def lng_subs(word:str):
   ds={}
   for x in word:
       if x not in ds:
           ds[x]=''
   for x in ds.keys():
      w=''.join(ds.keys())

   return w,len(w)






resp=lng_subs('abcabcbb')
print(resp)





