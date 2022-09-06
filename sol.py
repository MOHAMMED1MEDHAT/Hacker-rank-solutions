# def next_mul(x):
#     y=x//5
#     z=(y+1)*5
#     return z

# def round(x):
#     if next_mul(x)-x>3 and x>=38:return next_mul(x)
#     return x



# #grades=[73,67,38,33]


# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     dist_apl,dist_org=[],[]
#     num_apl_hit,num_org_hit=0,0
#     for i in apples:
#         dist_apl.append(a+i)
#     for i in oranges:
#         dist_org.append(b+i)
#     for x in dist_apl:
#         if x>=s and x<=t :
#             num_apl_hit=num_apl_hit+1
#     for y in dist_org:
#         if y>=s and y<=t  :
#             num_org_hit=num_org_hit+1
#     out_apl=str(num_apl_hit)
#     out_org=str(num_org_hit)
#     output=out_apl+"\n"+out_org
#     return output
            
        
# apl=[2,2,2]
# org=[-4,-4]
# def check_if_crach(x1,v1,x2,v2):
#     #first
#     #NUM-1
#     if x1>x2 and v1>v2:
#         if(x1-x2)%(v2-v1)!=0:
#             return "NO"
#         else:
#             return "NO"
#     #NUM-2
#     elif x1>x2 and v1==v2:
#         if(x1-x2)%(v2-v1)!=0:
#                 return "NO"
#         else:
#             return "NO"
#     #NUM-3
#     elif x1>x2 and v2>v1:
#         if(x1-x2)%(v2-v1)!=0:
#                 return "NO"
#         else:
#             return "YES"
#     #second
#     #NUM-4
#     elif x1==x2 and v1==v2:
#         if(x1-x2)%(v2-v1)!=0:
#                 return "NO"
#         else:
#             return "YES"
#     #NUM-5
#     elif x1==x2 and v1>v2:
#         if(x1-x2)%(v2-v1)!=0:
#                 return "NO"
#         else:
#             return "NO"
#     #NUM-6
#     elif x1==x2 and v2>v1:
#         if(x1-x2)%(v2-v1)!=0:
#                 return "NO"
#         else:
#             return "NO"
#     #third
#     #NUM-7
#     elif x2>x1 and v1==v2:
#         if(x1-x2)%(v2-v1)!=0:
#                 return "NO"
#         else:
#             return "NO"
#     #NUM-8
#     elif x2>x1 and v1>v2:
#         if(x1-x2)%(v2-v1)!=0:
#                 return "NO"
#         else:
#             return "YES"
#     #NUM-9
#     elif x2>x1 and v2>v1:
#         if(x1-x2)%(v2-v1)!=0:
#                 return "NO"
#         else:
#             return "NO"

# #print(check_if_crach(43,2,70,2))

def sort(x):
    n=len(x)
    for i in range(n):
      for j in range(0,n-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    return x

def no_repitions(x):
    for i in x:
        if x.count(i)>1:
            x.remove(i)    
    return x


def find_factors(a):
    fact=[]
    for x in a:
        for i in range(1,x):
            if x%i==0:
                fact.append(i)            
    return fact

def count_hcf(fact,y):
    c_f=[]
    for i in fact:
        if fact.count(i)==len(y):
            c_f.append(i)
    sort(c_f)
    return c_f[-1]
            
def count_lcm(y):
    m=[]
    c_m=[]
    for  i in y :
       for j in range(2,i):
           m.append(i*j)
    for x in m:
        if m.count(x)==len(y):
            c_m.append(x)
           
    sort(c_m)
    return c_m[0]

def gettotalx(a,b):
    lcm_a=count_lcm(a)
    hcf_b=count_hcf(find_factors(b),b)
        
    pass

#print(no_repitions(find_factors([24,36])))

result=count_hcf(find_factors([16,32,96]),[16,32,96])
print(result)
result=count_lcm([2,4])
print(result)



#print(no_repitions([1,1,2,3]))

# def add_mozes(x,y):
#     if (x+y)>7 and (x+y)<15:
#         return x+y-8
#     return x+y

# #print(add_mozes(9,6))
# def take_input():
#     st_in=input()
#     st_in.split(" ")
#     x,y=st_in[0],st_in[2]
#     return x,y


# x,y=1,1
# while y and x:
#     x,y=take_input[0],take_input[1]
#     print(add_mozes(int(x),int(y)))
    
# l=[1,2,1,21,2,12,11,11,11,22,11,22,111,1212,1]
# print(no_repitions(l))