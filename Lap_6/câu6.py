#1
m=int(input("Nhập số hàng : "))
n=int(input("Nhập số cột : "))
matran=[]
for i in range(1,m+1):
    row=[]
    for j in range(1,n+1):
        phantu=int(input(f"Nhập các phần tử của ma trận ở vị trí [{i},{j}] : "))
        row.append(phantu)
    matran.append(row)
print(f"Ma trận cơ {m}x{n} là: {matran}")
#2
sum = 0
for i in range(len(matran)):
    for j in range(len(matran[i])):
        sum += matran[i][j]
print("Tổng của các phần tử của ma trận là:", sum)
#3
#Nhập ma trận thứ 2
a=int(input("Nhập số hàng của ma trận 2 : "))
b=int(input("Nhập số cột của ma trận 2 : "))
matran2=[]
for i in range(1,a+1):
    roll=[]
    for j in range(1,b+1):
        phantu2=int(input(f"Nhập các phần tử của ma trận 2 ở vị trí [{i},{j}] : "))
        roll.append(phantu2)
    matran2.append(roll)
print("ma trận thứ 2 là : ",matran2)
#Tính tích 2 ma trận
if m!=b:
    print("Không thể tính ")
else:
    ketqua=[]
    for i in range(m):
        hang=[]
        for j in range(b):
            tich=0
            for k in range(n):
                tich=tich+matran[i][k]+matran2[k][j]
            hang.append(tich)
        ketqua.append(hang)

print(f"tích của 2 ma trận {matran}*{matran2} = ",ketqua)