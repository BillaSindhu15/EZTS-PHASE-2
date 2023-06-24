queue=[]
def enqueue():
    a=int(input("Enter the number:"))
    queue.append(a)
    print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("\ndeleted element is :",e)
        print(queue)
def display():
    if not queue:
        print("queue is empty")
    else:
        print(queue)
def peek():
    print(queue[-1])
while True:
    print("\n1.enqueue\n2.dequeue\n3.display\n4.peek\n5.quit")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        break
    else:
        print("\nInvalid input")
