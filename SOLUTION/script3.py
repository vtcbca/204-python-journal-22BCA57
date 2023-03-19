def  strfun(lis):
    a1=0
    for i in lis:
        a=len(i)
        if a%2==0:
            print(f'{i}')
            a1+=1
    print(f'Total Number Of Even Number Of Character  : {a1}')
lis=['om','sai','ram','ramesh','suresh']
strfun(lis)
