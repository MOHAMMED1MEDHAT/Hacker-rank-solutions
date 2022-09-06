def viralAdvertising(n):
    c=5
    result=0
    while n:
       c=c//2
       result=result+c
       c=c*3
       n=n-1 
    return result  
n=5
print(viralAdvertising(n))