def palin(a):
    m=a[::-1]
    if a==m:
        print(f'{a} is palindrome word')
    else:
        print(f'{a} is not palindrome word')
a=input('ENTER NAME ::')
palin(a)
