def catAndMouse(x, y, z):
    catA=abs(x-z)
    catB=abs(y-z)
    if catA<catB:
        return "Cat A"
    if catA>catB:
        return "Cat B"
    if catA==catB:
        return "Mouse C"
x=2
y=5
z=4
print(catAndMouse(x,y,z))