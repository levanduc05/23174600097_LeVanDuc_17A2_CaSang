#Tính S4
def tinh_tong_S4(n):
    tong = 0.0
    for i in range(1, n + 1):
        tong += ((-1) ** (i + 1)) / i
    
    return tong
def nhap_so_nguyen_duong():
    while True:
        try:
            n = int(input("Nhập số nguyên dương n: "))
            if n <= 0:
                print("Vui lòng nhập số nguyên dương lớn hơn 0.")
            else:
                return n
        except ValueError:
            print("Vui lòng nhập một số nguyên dương.")

def main():
    n = nhap_so_nguyen_duong()
    tong_S4 = tinh_tong_S4(n)
    print("Tổng của 1 - 1/2 + 1/3 - 1/4 + ... + (-1)^(n+1)/n là: {:.6f}".format(tong_S4))

if __name__ == "__main__":
    main()