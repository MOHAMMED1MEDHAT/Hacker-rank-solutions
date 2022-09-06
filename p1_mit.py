#بسم الله الرحمن الرحيم  
#problem1-2::
#+++++++++++++++++++++++++++++++++++++
#1-algo swap ends at any datastructure: 
#swap_ends(D):
#x1=D.delet_first()
#x2=D.delet_last()
#D.insert_fisrt(x2)
#D.insert_last(x1)
#++++++++++++++++++++++++++++++++
#2-algo shift left by one k times:
#shift_left(D,k):
#if k<1 or k>len(D)-1:
#   return
#x=D.delet_first()
#D.insert_last(x)
#shift_left(D,k-1)
#++++++++++++++++++++++++++++++++++++++
#3-algo double-ended sequence operations:
#use two list
#+++++++++++++++++++++++++++++++++++++++
#4-algo to jen&berry's:
# a_define a linked list 
# b_take the 2n items and put them in the list
# c_find the N'th item 
# d_reverse nodes from thier
#   .itiate a prev variable that points the previous item 
#   .make the last item points the n'th item 
#   .do this for all n+ items
#   .n+1 item should points "null"
# e_return the finished linked list 
#
class node:
    def __init__(self,data):
        self.data=data
        self.next=next
        
    def set_next(self,newnode):
        self.next=newnode
    def get_next(self):
        return self.next
    
    def set_data(self,newdata):
        self.data=newdata
    def get_data(self):
        return self.data
    
    def laster_node(self,i):
        if i==0 : return self
        assert self.next
        return self.next.laster_node(i-1)
    
class linked_list(node):
    def __init__(self):
        self.head=None
        self.size=0
    
    def add(self,item):
        temp=node(item)
        temp.set_next(self.head)
        self.head=temp
        
        
    def __len__(self):
        current=self.head
        while current.get_next()!=None:
            current=current.get_next()
            self.size=self.size+1
        return self.size
    
def reorder_list(L):
    prev=L.head
    current=L.head
    
    
    
    return
l=linked_list()
l.add("mohammed")
print(l)
fan=[12,412,14214,4124114,52153,521]
max(fan)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#