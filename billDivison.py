def bonAppetit(bill, k, b):
    s=0
    for i in range (len (bill)):
        if i==k:
            continue
        else:
            s=s+bill[i]
    if b==s//2:
        return "Bon Appetit"
    else:
        return b-(s//2)
    
bill=[3,10,2,9]
k=1
b=7
print(bonAppetit(bill,k,b))

