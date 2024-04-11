#Câu a
n=int(input("Nhập số n vào : "))
a=1
S1=0
S3=0
S4=0
while a<n:
    if n<=10:
        print("n nhỏ quá òi")
        break
    else:
        S1=S1+6**a
        S3=S3+((-1)**2)*(a**2)
        S4=S4+a*(a+1)*(a+2)
        a+=1
print(S1)    
#Câu b
a=0
S2=0
if n<=10:
    print("n không hợp lệ")
else:
    while a<n:
       S2=S2+1/(3**(2*a+1))
       a+=1
print(S2)
print(S3)
print(S4)