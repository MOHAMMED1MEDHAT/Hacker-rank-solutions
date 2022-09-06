def angryProfessor(k, a):
    c=0
    for i in a:
        if i <=0:
            c=c+1
    if c>=k:
        return "NO"
    else:
        return "YES"


k=2
a=[0 ,-1 ,2 ,1]
print(angryProfessor(k,a))