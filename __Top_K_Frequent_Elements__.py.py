#__Top_K_Frequent_Elements__.py
def topk(ls:list[int],k:int):
    ds={}
    s=[]
    for x in ls:
        if x not in ds:
            ds[x]=1
        else:
            ds[x]+=1
    for x,y in ds.items():
        if y==k:
           s.append(x)
    return s



resp=topk([1, 1, 1, 2, 2, 3],2)
print(resp)
    





