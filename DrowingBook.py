def pageCount(n, p):
    flipsPossible = (n // 2)
    # if(p%2 !=0):
    #     fromStart=(p//2)+1
    #     fromEnd=flipsPossible-((p//2)+1)
    # else:
    #     fromStart=(p//2)
    #     fromEnd=flipsPossible-(p//2)
    fromStart = (p // 2)
    fromEnd = flipsPossible - (p // 2)

    if (p == 1):
        return 0
    if ((p == n and n % 2 == 0) or (p == n - 1 and n % 2 != 0)):
        return 0
    if (fromStart < fromEnd and fromStart > 0):
        return fromStart
    return fromEnd
print(pageCount(10,8))