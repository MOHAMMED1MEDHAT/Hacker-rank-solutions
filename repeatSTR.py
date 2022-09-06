def repeatedString(s, n):
    result=0
    result+=(n//len(s))*s.count("a")
    s=s[:(n-(len(s)*(n//len(s))))]
    result+=s.count("a")
    return result
s="ababbbaabbaaaba"
n=100
print(repeatedString(s,n))
print(len(s))
print(s.count("a"))
 # ss=s
    # if len(s)>1:
    #     s+=(s*(n//len(s)))
    # else:
    #     return n
    # if len(ss)>1:
    #     s=s[:n]
    # return s.count("a")
    # result=((s.count("a")/len(s))*n) 
    # res=str(result)
    # re=res.split(".")
    # if float(re[1])>0.5:
    #     return ceil(result)
    # elif 0.5 >float(re[1])>0 :
    #     return floor(result)
    # else:
    #     return int(result)