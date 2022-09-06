def sum(s):
    n=int(s)
    if (n==1) : return 1
    return n+sum(n-1)
#n=input("enter the number")
#print ("sum of {0} is {1}".format(n,sum(n)))

#second problem
def grad_path(a,b):
    n=int(a)
    m=int(b)
    if (n==1 or m==1): return 1
    return grad_path(n,m-1)+grad_path(n-1,m)

#n=input("enter the first number ")
#m=input("enter the second number ")
#print ("the posspality of the grid({0},2{1}) is {2} shapes".format(n,m,grad_path(n,m)))

#third problem
def count_partitions(a,b):
    n=int(a)
    m=int(b)
    if n==0 :return 1
    if m==0 or n<0 :return 0
    return count_partitions(n-m,m)+count_partitions(n,m-1)

n=input("enter the first number")
m=input("enter the second number")
print(" number of partitions on {0} using {1} is {2}".format(n,m,count_partitions(n,m)))
