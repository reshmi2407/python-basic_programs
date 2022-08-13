b=int(input("Enter the starting number:"))
e=int(input("Enter the ending number:"))
for n in range(b,e+1):
    flag=0
    if(n<0):
        flag=1
        break
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            flag=1

    if(flag==0):
        print(n)