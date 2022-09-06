import math

def squares(a, b):
    c=int(abs((math.sqrt(a)//1)-(math.sqrt(b)//1)))
    if math.sqrt(a)%1==0:
        c=c+1
    return c
a=100
b=1000
print(squares(a,b))
print(math.sqrt(a)//1)
print(math.sqrt(b)//1)
# x=[1,2,2,3,514,64,46,5,949,14,78]
# y=[1,2,2,3,514,64,46,5,949,14,78]
# plt.plot()
# plt.show()