stack=[]
even=[]
def push():
    a=int(input("Enter the number:"))
    stack.append(a)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("\ndeleted element is :",e)
        print(stack)
def display():
    if not stack:
        print("stack is empty")
    else:
        print(stack)
def peek():
    print(stack[-1])
    
def even():
    even=[]
    odd=[]
    if not stack:
        print("stack empty")
    else:
        for i in range(len(stack)):
            if stack[i]%2==0:
                even.append(stack[i])
            else:
                odd.append(stack[i])
        print(even)
        print(odd)        
        
    
    
        
while True:
    print("\n1.push\n2.pop\n3.display\n4.even\n5.peek\n6.quit")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        even()
    elif choice==5:
        peek()
    elif choice==6:
        break
    else:
        print("\nInvalid input")

