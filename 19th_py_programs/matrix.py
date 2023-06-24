r=int(input("Enter number of rows"))
c=int(input("Enter number of coloumns"))
matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        x=int(input("Enter the item"))
        a.append(x)
    matrix.append(a)
print(matrix)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=' ')
    print()
print("diagnol elements are:")    
for i in range(r):
    for j in range(c):
        if i==j:
            print(matrix[i][j],end=' ')
        else:
            print(" ",end=' ')
    print()
print("upper diagonal elements are:")    
for i in range(r):
    for j in range(c):
        if i<j:
            print(matrix[i][j],end=' ')
        else:
            print(" ",end=' ')
    print()
print("lower diagonal elements are:")    
for i in range(r):
    for j in range(c):
        if i>j:
            print(matrix[i][j],end=' ')
        else:
            print(" ",end=' ')
    print()      
print("non diagonal elements are:")    
for i in range(r):
    for j in range(c):
        if i!=j:
            print(matrix[i][j],end=' ')
        else:
            print(" ",end=' ')
    print()
print("transpose")
for i in range(r):
    for j in range(c):
        print(matrix[j][i],end=' ')
    print()