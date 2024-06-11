#First_Non-Repeating_Character
def Fi(word:str):
   ds={}
   ls=[]
   for x in word:
       if x not in ds:
           ds[1]=x
       else:
           ds[=+1]=''
   
   return ds[1]



resp=Fi('AAHeello')
print(resp.items())
