class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue():
    def __init__(self):
        self.head=None
    def enqueue(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            ne=Node(data)
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=ne
            ne.next=None
            
        
        
    def dequeue(self):
        if self.head is None:
            print("queue is empty")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            print("deleted element is ",temp.data)
    def display(self):
        if self.head is None:
            print("queue is empty")
        else:
            temp=self.head#temp=first node
            while temp:
                 print(temp.data,end=" ")
                 temp=temp.next       
obj=queue()
while True:
    print("\n1.enqueue\n2.dequeue\n3.display\n4.peek\n5.quit")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        a=int(input("Enter the element"))
        obj.enqueue(a)
    elif choice==2:
        obj.dequeue()
    elif choice==3:
        obj.display()    
    elif choice==4:
        if obj.head==None:
            print("queue is empty")
        else:
            print("the element is",obj.head.data)
    elif choice==5:
        break
    else:
        print("\nInvalid input")

            
        
        
            
