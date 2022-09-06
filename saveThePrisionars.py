def saveThePrisoner(n, m, s):
    # result=s
    # c=0
    # for i in range(1,m+1):
    #     if i%n==0:
    #         c=0
    #     if result<c:
    #         result=c
    #     c=c+1
    # if s+m<=n:
    #     return result+1
    # else:
    #     return result
    # if s+m<=n:
    #     return (s+m-1)
    # else:
    #     if (m%n)+s<=n+1:
    #         return (m%n)+s-1
    #     else:
    #         return (m%n)+s-n-1
    return ((s-1+m-1)%n )+1
n=3
m=7
s=3
print(saveThePrisoner(n,m,s))
print(m%n)