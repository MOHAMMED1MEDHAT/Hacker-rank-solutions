def extraLongFactorials(n):
    # this the recursion way and the most efficient way
    if n>1:
        return extraLongFactorials(n-1)*n
    if n==1:
        return n
    # result=1
    # for i in range(1,n+1):
    #     result=result*i
    # return result
n=25
print(extraLongFactorials(n))