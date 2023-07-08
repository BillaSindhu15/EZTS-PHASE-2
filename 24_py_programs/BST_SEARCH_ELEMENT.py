class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
        return root
def Search(root,key):
    if root is None or root.val==key:
        return root
    if root.val<key:
        return Search(root.right,key)
    return Search(root.left,key) 


r = None
n=int(input('Enter no of elements to insert:'))
for i in range(0,n):
    if r is None:
        item=int(input("Enter item:"))
        r=Node(item)
    else:
        item=int(input("Enter item:"))
        r=insert(r,item)
key = int(input("Enter the search element: "))
result = Search(r, key)

if result is None:
    print("Not present")
else:
    print("present")

