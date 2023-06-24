#Creating Node declaration & defination
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
        
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=ne
        ne.next=None
        
        
    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
        
    def delete_end(self):
        temp=self.head
        while temp.next!=None:
            ptr=temp
            temp=temp.next
        ptr.next=None
        
        
    def delete_position(self):
        
        temp=self.head
        loc=int(input("Enter location:"))
        c=1
        while temp!=None and c!=loc:
            ptr=temp
            c+=1
            temp=temp.next
        if temp==None:
            print("location not found")
        else:
            print("deleted element:",temp.data)
            ptr.next=temp.next
            
        
         
        
    
    
    def insert_position(self,data):
        np=Node(data)
        temp=self.head
        loc=int(input("Enter location:"))
        c=1
        if loc==1:
            nb=Node(data)
            nb.next=self.head
            self.head=nb
        else:
            while temp!=None and c!=loc:
                ptr=temp
                c+=1
                temp=temp.next
            ptr.next=np
            np.next=temp
            
    def search(num):
        temp=self.head
        while temp:
            if temp.data==num:
                print("yes")
                break
            temp=temp.next
                
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head#temp=first node
            while temp:
                 if temp.next!=None:
                     print(temp.data,"->",end=' ')
                 else:
                     print(temp.data,end=' ')
                 temp=temp.next
obj=singlelinkedlist()
n=Node(10)#so n.data in node class will be 10
obj.head=n   #assigning first node as head
n1=Node(20)
obj.head.next=n1  #next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
obj.display()
print("\nDelete at begin\n")
obj.delete_begin()
print(" ")
obj.display()
print("\nDelete at end\n")
obj.delete_end()
print(" ")
obj.display()
print("\nDelete at position\n")
obj.delete_position()
print(" ")
obj.display()
num=int(input("Enter the number"))
obj.search(num)
print(" ")
obj.display()
    



