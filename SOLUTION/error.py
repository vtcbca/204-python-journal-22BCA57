n=int(input('enter no of elements you want to enter in list ::'))
lis=[]
for i in range(n):
    a=input(f'enter elements[{i}] ::')
    lis.append(a)
for i in range(len(lis)):
    for j in range(len(lis[i])):
        if j%2==0:
            lis[i][j]=str(j)
print(lis)
            
            
