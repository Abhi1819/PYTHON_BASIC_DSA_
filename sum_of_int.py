def sum_of(ls:list[int],target):
   ds={} 
   for x in range(len(ls)):
      rem=target-ls[x]
      if rem in ls[x+1:]:
        ds[ls[x]]=rem
        

   print(ds.items())





resp=sum_of([1,2,3,42,4,5,6,7,8,9,10],10)


