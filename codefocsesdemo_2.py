#  def check_even(x):
#      if x%2==0 and (x!=2):
#          return "YES"
#      return "NO"
#  x=int(input())
#  print(check_even(x))
# i=int(input())
# wordl=[]
# for y in range(i):
#     wordl.append(input())
# def shrink(wordl):
#     new_word=list(wordl)
#     for x in wordl:
#         word=x
#         if len(word)>10:
#             new_word[wordl.index(x)]=f"{word[0]}{len(word)-2}{word[-1]}"
    
#     return new_word
# result=shrink(wordl)
# for i in result:
#     print(i)
#================================================
# test=int(input())
# count=0
# while test>0:
#     st_in=input()
#     st_list=st_in.split(" ")
#     x,y,z=int(st_list[0]),int(st_list[1]),int(st_list[2])
#     if(x and y)or (x and z) or (y and z):
#         count=count+1
#     test=test-1
# print(count)
#=======================================================
# st=input()
# l_in=st.split(" ")
# st_scores=input()
# l_score=st_scores.split(" ")
# x,n=int(l_in[1]),int(l_in[0])
# min=int(l_score[x-1])
# count=0
# for i in range(0,n):
#     if int(l_score[i])>= min and int(l_score[i])>0:
#        count=count+1 
# print(count)
#==============================
# st=input()
# l=st.split(" ")
# print(int(l[0])-int(l[1]))
map=[['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','m','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
     ['-','-','-','-','-','-','-','p','-','-','-','-','-','-','-'],]
n=15
xp,yp,xm,ym,up,down,right,left=0,0,0,0,0,0,0,0
#to detect the princes and the bot
for x in range(0,n):
    for y in range(0,n):
        if ord(map[y][x])==109:
            xm,ym=x,y
        elif ord(map[y][x])==112:
            xp,yp=x,y
print(yp,xp,ym,xm)
# to calculate the distance between the bot and the princes
x=xm-xp
y=ym-yp
if y<0:
    up=-y
if y>0:
    down=y
if x<0:
    left=-x
if x>0:
    right=x
#to return the root for the bot
root=""
for i in range(0,down):
    root=root+"Up"+"\n"
for i in range(0,up):
    root=root+"Down"+"\n"
for i in range(0,left):
    root=root+"Right"+"\n"
for i in range(0,right):
    root=root+"Left"+"\n"
print(root)