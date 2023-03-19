def palin(a):
    m=a.split(' ')
    a1=0
    for i in range(len(m)):
        if m[i]==m[i][::-1]:
            print(f'{m[i]}')
            a1+=1
    print(f'total number of palindrome in string is {a1}')
a=input('ENTER  STRING ::')
palin(a)    
