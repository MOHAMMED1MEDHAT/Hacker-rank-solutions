count =2

def x_y(x,y,z):
    count=0
    if x==y and count>=0:
        count -=1
        return x
    else:
        x_i_y(x,y,z)
    
def z_y(x,y,z):
    if z==y:
        return z
    else :
        z_i_y(x,y,z)
    
def x_z(x,y,z):
    if x==z:
        return  z
    else :
        x_i_z(x,y,z)
    
def x_i_y(x,y,z):
    if x!=y:
        return x_y(x,y,z),z_y(x,y,z)
    
def x_i_z(x,y,z):
    if x!=z:
        return x_z(x,y,z),z_y(x,y,z)
    
def z_i_y(x,y,z):
    if z!=y:
        return z_y(x,y,z),x_y(x,y,z)
    
    
x=input("enter x:")
y=input("enter y:")
z=input("enter z:")
print(x_y(x,y,z),x_z(x,y,z),z_y(x,y,z))