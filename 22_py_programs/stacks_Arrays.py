stack=[]
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
while True:
    print("\n1.push\n2.pop\n3.display\n4.peek\n5.quit")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        break
    else:
        print("\nInvalid input")