def getMoneySpent(keyboards, drives, b):
    prices=[]
    possibleToBuy=[]
    for keyboard in keyboards:
        for drive in drives:
            prices.append(keyboard+drive)
    
    for price in prices:
        if price <=  b:
            possibleToBuy.append(price)
    # for i in range(0,len(possibleToBuy)):
    #     for j in range(0,len(possibleToBuy)-i-1):
    #         if possibleToBuy[j+1]<possibleToBuy[j]:
    #             possibleToBuy[j],possibleToBuy[j+1]=possibleToBuy[j+1],possibleToBuy[j]
    if len(possibleToBuy)==0:
        return -1            
    else:
        return max(possibleToBuy)

keyboards=[3,1]
drives=[5,2,8]
b=10
print (getMoneySpent(keyboards,drives,b))