def Norepeat(anyList):
    for item in anyList:
        if anyList.count(item)>1:
            anyList.remove(item)
    return anyList

def calcNSum(square):
    sum=[]
    sum.append(square[0][0]+square[0][1]+square[0][2])#zero sum 
    sum.append(square[1][0]+square[1][1]+square[1][2])#1 sum
    sum.append(square[2][0]+square[2][1]+square[2][2])#2 sum
    sum.append(square[0][0]+square[1][1]+square[2][2])#3 sum
    sum.append(square[0][2]+square[1][2]+square[2][2])#4 sum
    sum.append(square[0][1]+square[1][1]+square[2][1])#5 sum
    sum.append(square[0][0]+square[1][0]+square[2][0])#6 sum
    sum.append(square[0][2]+square[1][1]+square[2][0])#7 sum
    return Norepeat(sum)

def calcSum(square):
    sum=[]
    sum.append(square[0][0]+square[0][1]+square[0][2])#zero sum 
    sum.append(square[1][0]+square[1][1]+square[1][2])#1 sum
    sum.append(square[2][0]+square[2][1]+square[2][2])#2 sum
    sum.append(square[0][0]+square[1][1]+square[2][2])#3 sum
    sum.append(square[0][2]+square[1][2]+square[2][2])#4 sum
    sum.append(square[0][1]+square[1][1]+square[2][1])#5 sum
    sum.append(square[0][0]+square[1][0]+square[2][0])#6 sum
    sum.append(square[0][2]+square[1][1]+square[2][0])#7 sum
    return sum

def assignLs(square):
    L=[ [square[0][0],square[0][1],square[0][2]]
       ,[square[1][0],square[1][1],square[1][2]]
       ,[square[2][0],square[2][1],square[2][2]]
       ,[square[0][0],square[1][1],square[2][2]]
       ,[square[0][2],square[1][2],square[2][2]]
       ,[square[0][1],square[1][1],square[2][1]]
       ,[square[0][0],square[1][0],square[2][0]]
       ,[square[0][2],square[1][1],square[2][0]]]
    return L

def calcOmiga(s):
    omiga=[]
    som=calcSum
    sumRows=0
    rows=assignLs(s)
    for item in calcSum(s):
        for i in range (0,8):
            for j in range(0,3):
                sumRows=sumRows+rows[i][j]
            W=item-sumRows
            omiga.append(W)
            sumRows=0
    return omiga
     
def formingMagicSquare(s):
    res=[]
    som=calcSum(s)
    rows=assignLs(s)
    omiga=calcOmiga(s)
    for item in calcNSum(s):
        for i in range (0,8):
            for j in range(0,3):
                if som[i]>=item: 
                    res.append(rows[i][j]-omiga[i])
                else:
                    res.append(rows[i][j]+omiga[i])
    for item in calcNSum(s):
        pass
    return     res

        
               
square=[ [4,8,2]
        ,[4,5,7]
        ,[6,1,6]]


#print(formingMagicSquare(square))
#print(calcSum(square))
#print(calcOmiga(square))

l=[0, -2, 1, -1, -1, 0, 0, 1, 2, 0, 3, 1, 1, 2, 2, 3, -1, -3, 0, -2, -2, -1, -1, 0, 1, -1, 2, 0, 0, 1, 1, 2, 1, -1, 2, 0, 0, 1, 1, 2, 0, -2, 1, -1, -1, 0, 0, 1, 0, -2, 1, -1, -1, 0, 0, 1, -1, -3, 0, -2, -2, -1, -1, 0]
s=[]
small=[]
sum=0
result=[]
som=calcSum(square)
L=assignLs(square)
for i in range (0,len(som)):#length of sum
    for j in range (0,len(som)):
        if l[i*len(som)+j]==0:
            small.append(0)
        small.append(abs(L[i][0]-l[i*len(som)+j]))
        small.append(abs(L[i][1]-l[i*len(som)+j]))
        small.append(abs(L[i][2]-l[i*len(som)+j]))
        sum=sum+min(small)
        s.append(sum)
        small=[]
    sum=0
for i in range(0,len(som)):
    for j in range(0,len(som)):
        sum=sum+s[i*len(som)+j]
    result.append(sum)
    sum=0
print(result)
    
