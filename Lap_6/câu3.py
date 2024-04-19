chuoi_so = input("Nhập dãy số, cách nhau bằng dấu cách: ").split()

so_thuc = [float(so) for so in chuoi_so]

so_lon_nhat = max(so_thuc)
so_nho_nhat = min(so_thuc)

print("Số lớn nhất trong dãy số là:", so_lon_nhat)
print("Số nhỏ nhất trong dãy số là:", so_nho_nhat)
