def appendAndDelete(s, t, k):
    sList,tList=[],[]
    cr,c=0,0
    s_idx,t_idx=0,0
    for i in s:
        sList.append(i)
    for i in t:
        tList.append(i)
    if len(sList)>=len(tList):
        for idx,i in enumerate(tList):
            if sList[idx]==i:
                sList[idx]=0
                tList[idx]=0
        for i in range(0, len(sList)):
            if sList[i]!=0:
                if c==0:
                    s_idx=i
                c=c+1
        cr,c=c,0
        for i in range(0, len(tList)):
            if tList[i]!=0:
                if c==0:
                    t_idx=i
                c=c+1
        c=c+cr
        if sList[-1]==tList[t_idx]:
            c=c-2
    else:
        for idx,i in enumerate(sList):
            if tList[idx]==i:
                sList[idx]=0
                tList[idx]=0
        for i in range(0, len(sList)):
            if sList[i]!=0:
                if c==0:
                    s_idx=i
                c=c+1
        cr,c=c,0    
        for i in range(0, len(tList)):
            if tList[i]!=0:
                if c==0:
                    t_idx=i
                c=c+1
        c=c+cr
        if tList[-1]==sList[s_idx]:
            c=c-2
    if c<=k:
        return "Yes"
    else:
        return "No"
    # for ops_left in reversed(range(1, k + 1)):
    #     if s == t[:len(s)] and len(t) - len(s) == ops_left or len(s) == 0:
    #         break
    #     s = s[:-1]
    #     if (len(t) - len(s)) <= ops_left: 
    #         return "Yes"
    #     else:
    #         return"No"
    
        
s='hackerkiller'
t='hackerrank'
k=9
print(appendAndDelete(s,t,k))