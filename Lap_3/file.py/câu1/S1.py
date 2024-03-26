# tính S1
def tinh_tong(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i
    
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
    tong = tinh_tong(n)
    print("Tổng của 1 + 2 + 3 + ... +", n, "là:", tong)

if __name__ == "__main__":
    main()