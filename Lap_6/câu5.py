day_so = input("Nhập dãy số nguyên, cách nhau bằng dấu cách: ").split()

day_so_nguyen = [int(so) for so in day_so]
la_cap_so_cong = True
if len(day_so_nguyen) < 3:
    la_cap_so_cong = False
else:
    for i in range(2, len(day_so_nguyen)):
        if day_so_nguyen[i] - day_so_nguyen[i - 1] != day_so_nguyen[1] - day_so_nguyen[0]:
            la_cap_so_cong = False
            break
if la_cap_so_cong:
    print("Dãy số tạo thành cấp số cộng:", day_so_nguyen)
else:
    print("Dãy số không tạo thành cấp số cộng.")
