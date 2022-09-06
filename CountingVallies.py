def countingValleys(steps, path):
    count=0
    res=0
    for step in path:
        if step=="U" and count <0:
            count=count+1
        if step=="D" :
            count=count-1
        if count == 0 and step!="D":
            res=res+1
    return res


print(countingValleys(12, "DDUUDDUDUUUD"))