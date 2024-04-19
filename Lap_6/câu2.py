n = int(input("Nhập số lượng phần tử trong mảng: "))
arr = []
print("Nhập các phần tử của mảng:")
for i in range(n):
    num = int(input(f"Phần tử {i+1}: "))
    arr.append(num)

print("\nCác số nguyên tố trong mảng:")
nguyen_to = []
for num in arr:
    if num > 1:
        la_nguyen_to = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            nguyen_to.append(num)
print(nguyen_to if nguyen_to else "Không có số nguyên tố nào trong mảng.")

print("\nCác số hoàn hảo trong mảng:")
so_hoan_hao = []
for num in arr:
    if num > 1:
        tong_uoc = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                tong_uoc += i
                if i != num // i:
                    tong_uoc += num // i
        if tong_uoc == num:
            so_hoan_hao.append(num)
print(so_hoan_hao if so_hoan_hao else "Không có số hoàn hảo nào trong mảng.")
