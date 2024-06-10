def intersection(list1, list2, ds={}):
    intersection_values = []
    for x in list1:
        if x in list2 and x not in intersection_values:
            intersection_values.append(x)
    ds['intersection'] = intersection_values
    return ds

resp = intersection([1, 2, 2, 3, 4, 5], [2, 2, 3, 5, 6, 7])
print(resp)



