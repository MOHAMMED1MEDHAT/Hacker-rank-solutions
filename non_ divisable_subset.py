from tkinter.messagebox import NO


from itertools import combinations 

def nonDivisibleSubset(k, s):
    result_list=[]
    comb=combinations(s,2)
    for i in list(comb):
        if (i[0]+i[1])%k!=0:
            result_list.append(i[0])
            result_list.append(i[1])
    return result_list

s=[19,10,12,10,24,25,22]
k=4
print(nonDivisibleSubset(k,s))