#Câu a
a=2
while a<100:
    check=True
    b=2
    while b**2<=a:
        if a%b== 0:
            check=False
            break
        b+= 1
    if check==True:
        print(a, end=" ")
    a+= 1

#Câu b
a=1
while a<100:
    b=int(a**0.5)
    if b**2==a:
        print(a,end=" ")
    a+=1