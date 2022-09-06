def cutTheSticks(arr,res):
    if len(arr)>1:
        c=min(arr)
        for i in range(len(arr)):
            arr[i]=arr[i]-c
        for i in arr:
            if i==0:
                coun=arr.count(i)
                for j in range(coun):
                    arr.remove(i)
        res.append(len(arr))
        return cutTheSticks(arr,res)
    elif len(arr)<=1 :
        if res[-1]==0:  res.remove(0)
        return res

arr=[5,4,4,2,2,54,6,54,16,54,54,65,46,5644,654,456,464]
res=[len(arr)]
print(cutTheSticks(arr,res))
# def milesToKilometers(miles):
#     kilometers = miles*1.60934
#     dump() # dumps all the vars in your function

#     # or dump when function is called for a second time
#     d
# Write your code here
def returnn(res):
    res=[len(arr)]
    length=len(arr)
    for i in range(0,length):
        c=min(arr)
        for j in (0,length):
            arr[j]=arr[j]-c
            if arr[j]==0:
                arr.remove(arr[j])
            length=len(arr)
            res.append(length)
    return res