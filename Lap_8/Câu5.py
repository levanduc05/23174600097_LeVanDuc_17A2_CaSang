def tongUocSoChinh(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def laSoAmicable(a, b):
    return tongUocSoChinh(a) == b and tongUocSoChinh(b) == a

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

if laSoAmicable(a, b):
    print(f"{a} và {b} là số amicable.")
else:
    print(f"{a} và {b} không phải là số amicable.")
