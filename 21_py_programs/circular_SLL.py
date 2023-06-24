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
#Node creation-initialising
n=Node(10)#so n.data in node class will be 10
obj.head=n   #assigning first node as head
n1=Node(20)
obj.head.next=n1  #next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
n5.next=n
print("before inserting 100")
obj.display()
print(" ")
print("after inserting 100")

obj.insert_beginning(100)

obj.display() #traverse
print(" ")
print("after inserting 555")
obj.insert_beginning(555)
obj.display()
print(" ")
print("insert at end")
obj.insert_end(80)
obj.display()
print("Insert at position")
obj.insert_position(99)
obj.display()





