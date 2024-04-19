n = int(input("Nhập số Fibonacci bạn muốn tạo: "))
danh_sach_fibonacci = [0, 1] if n > 1 else [0] if n == 1 else []

if n > 2:
    for i in range(2, n):
        danh_sach_fibonacci.append(danh_sach_fibonacci[-1] + danh_sach_fibonacci[-2])

print("Dãy Fibonacci:", danh_sach_fibonacci)

danh_sach_so_nguyen_to = [so for so in range(2, 100) if all(so % i != 0 for i in range(2, int(so ** 0.5) + 1))]

print("Danh sách số nguyên tố nhỏ hơn 100:", danh_sach_so_nguyen_to)


