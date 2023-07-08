a=[1,2,3,4,5,6,7,8,9,10]
e=3
l=0
h=9
f=0
for i in a:
    m=int((l+h)/2)
    if(e==a[m]):
        print("element found at location",m)
        f=1
        break
    elif(e<a[m]):
        h=m-1
    else:
        l=m+1
if(f==0):
    print("element not found")