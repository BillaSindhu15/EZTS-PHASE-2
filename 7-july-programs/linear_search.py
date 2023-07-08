#linear search
arr=[5,2,3,7,3,5,4,8,5,67,4]
key=7
found=False
for index in range(len(arr)):
    if arr[index]==key:
        print("element found",index)
        found=True
        break
if found==False:
    print("element not found")