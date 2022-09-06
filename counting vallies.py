# def countingValleys(steps, path):  
#     count=0
#     res=0
#     C=0
#     sk=False
#     for i in range(0,steps):
#         if sk:
#             sk=False
#             C=C+1
#             continue
#         if path[i]=="U" :
#             if count<0:
#                 count=count+1
#                 sk=False
#             else:
#                 sk=True
#                 C=C+1
#                 continue
#         if path[i]=="D" :
#             count=count-1
#         if count == 0 :
#             res=res+1
        
#     return res 
def countingValleys(n, steps):
    seaLevel = valley = 0

    for step in steps:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        
        if step == 'U' and seaLevel == 0:
            valley += 1
    
    return valley
my_path=["D","D","D","U","D","U","U","U","U","D","U","D","D","D","D","U","U","U","D","U"]
path=len(my_path)
print(countingValleys(path,my_path))