def circularArrayRotation(a, k, queries):
    result=[]
    for i in range(0,k):
        a.insert(0,a[-1])
        a.pop(-1)
    for query in queries:
        result.append(a[query])
    return result
    
a=[3,4,5]
k=2
queries=[1,2]
print(circularArrayRotation(a,k,queries))