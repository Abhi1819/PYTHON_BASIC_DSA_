#__Subarray_Sum_Equals_K__.py
def subk(ls:list[int],k):
    l=[]
    rem=0
    count=0
    mid=k/2
    rem2=0
    for x in ls:
        if x <= k:
            count+=x
            rem=k-x
        for z in range(x+1,len(ls)-1):
            if ls[z] <= rem:
               count+=ls[z]
               if count==k:
                  l.append([x,z])
    return l


resp=subk([1, 1, 1, 2, 2, 3],4)
print(resp)
