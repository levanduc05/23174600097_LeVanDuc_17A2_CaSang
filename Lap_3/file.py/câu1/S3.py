#Tính S3
def tinh_tong_S3(n):
    tong = 0.0
    for i in range(1, n + 1):
        tong += 1 / ((2 * i)**0.5)
    
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
    tong_S3 = tinh_tong_S3(n)
    print("Tổng của 1/√2 + 1/√4 + ... + 1/√{} là: {:.6f}".format(2*n, tong_S3))

if __name__ == "__main__":
    main()