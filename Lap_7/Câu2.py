sinh_vien = {}
for i in range(1, 11):
    print(f"Nhập thông tin cho sinh viên thứ {i}:")
    ten = input("Tên sinh viên: ")
    diem = float(input("Điểm thi: "))
    sinh_vien[ten] = diem

xep_loai = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

for ten, diem in sinh_vien.items():
    if diem < 4.0:
        xep_loai['F'] += 1
    elif diem < 5.5:
        xep_loai['D'] += 1
    elif diem < 7.0:
        xep_loai['C'] += 1
    elif diem < 8.5:
        xep_loai['B'] += 1
    else:
        xep_loai['A'] += 1
print("\nXếp loại học lực và số lượng sinh viên ở mỗi loại:")
for xep_loai, so_luong in xep_loai.items():
    print(f"Xếp loại {xep_loai}: {so_luong} sinh viên")
