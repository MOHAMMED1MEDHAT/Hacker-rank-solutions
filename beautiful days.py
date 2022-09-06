def reverse(i):
    j=str(i)
    k=""
    x=[]
    for i in j:
        x.append(i)
    for i in range(0,len(x)):
        x.insert(i,x[-1])
        x.pop(-1)
    for i in x:
        k=k+str(i)
    return int(k)


def beautifulDays(i, j, k):
    c=0
    for x in range(i,j+1):
        if abs(x-reverse(x))%k==0:
            c=c+1
    return c
i=200
j=900
k=6
print(beautifulDays(i,j,k))