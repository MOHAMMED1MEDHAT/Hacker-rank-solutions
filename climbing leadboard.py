
def climbingLeaderboard(ranked, player):
    ranked=[i for n,i in enumerate(ranked) if i not in ranked[:n]]
    ranks=[]
    r=0
    for i in range(0,len(player)):
        for j in range(0,len(ranked)):
            if player[i]<ranked[j]:
                r=j+2
            elif player[i]>ranked[j]:
                r=j+1
                break
            elif player[i]==ranked[j]:
                r=j+1
                break
        ranks.append(r)
        ranked.insert(r-1,player[i])
        r=0
    return ranks
#=======================================================
def climbingLeaderboard(scores, alice):
    scores_set = list(set(scores))
    scores_set.sort(reverse=True)
    result = []
    l = len(scores_set)
    for s in alice:
        while (l>0) and (s >= scores_set[l-1]):
            l -= 1
        result.append(l+1)
    return result
a=[100,100,50,40,20,10]
b=[5,25,50,120]
print(climbingLeaderboard(a,b))