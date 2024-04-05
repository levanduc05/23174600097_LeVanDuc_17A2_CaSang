n = int(input("Nhập số từ bàn phím: "))
count = 1
a=n
while True: 
    a = a//10  
    if a == 0:
        break
    count += 1 

for i in range(count,0,-1):
    phan_nguyen = n//(10**(i-1))
    if phan_nguyen == 0:
        print("Zero", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 1:
        print("One", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 2:
        print("Two", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 3:
        print("Three", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 4:
        print("Four", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 5:
        print("Five", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 6:
        print("Six", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 7:
        print("Seven", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 8:
        print("Eight", end = " ")
        n = n % (10**(i-1))
    elif phan_nguyen == 9:
        print("Nine", end = " ")
        n = n % (10**(i-1))