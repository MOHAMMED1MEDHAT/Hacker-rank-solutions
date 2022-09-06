def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1-y2>0:
        return 10000
    elif m1-m2>0 and y1-y2==0:
        return 500*(m1-m2)
    elif d1-d2>0 and m1-m2==0:
        return 15*(d1-d2)
    else:
        return 0
    
d1,m1,y1=9,6,2015
d2,m2,y2=1,5,2015
print(libraryFine(d1,m1,y1,d2,m2,y2))