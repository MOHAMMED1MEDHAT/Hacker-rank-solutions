def pickingNumbers(a):
    # stringPreserve=""
    # result=[]
    # resultLenght=[]
    # for i in range(0,len(a)-1):
    #     if a[i+1]>(a[i]+1):
    #         stringPreserve=stringPreserve+str(a[i])+" "
    #     else:
    #         stringPreserve=stringPreserve+str(a[i])
    # if a[-1]>(a[-2]+1):
    #         stringPreserve=stringPreserve+" "+str(a[-1])
    # else:
    #     stringPreserve=stringPreserve+str(a[-1])
    # result=result+stringPreserve.split(" ")
    # for i in result:
    #     resultLenght.append(len(i))
    # return max(resultLenght),result
    maximum=0
    l=[]
    for i in range (0,len(a)):
        for j in range(0,len(a)-i-1):
            if abs(a[i]-a[i+j])==1:
                if maximum< (a.count(a[i])+a.count(a[i+j])):
                    maximum=maximum+a.count(a[i])+a.count(a[i+j])
                l.append(maximum)
        maximum=0
    
    return max(l)

a=[1,2,2,3,1,2]
print(pickingNumbers(a))