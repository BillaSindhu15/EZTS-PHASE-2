class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack():
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            nb=Node(data)
            nb.next=self.head
            self.head=nb
    def pop(self):
        if self.head is None:
            return "stack is empty"
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            print("deleted element is ",temp.data)
    def display(self):
        if self.head is None:
            print("stack is empty")
        else:
            temp=self.head#temp=first node
            while temp:
                 print('|',temp.data,'|')
                 temp=temp.next       
obj=stack()
while True:
    print("\n1.push\n2.pop\n3.display\n4.peek\n5.quit")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        a=int(input("Enter the element"))
        obj.push(a)
    elif choice==2:
        obj.pop()
    elif choice==3:
        obj.display()    
    elif choice==4:
        if obj.head==None:
            print("stack is empty")
        else:
            print("the element is",obj.head.data)
    elif choice==5:
        break
    else:
        print("\nInvalid input")

            
        
        
            