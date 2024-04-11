chuỗi = input("bấm vào bàn phím một chuỗi đi bạn ê: ")
kí_tự_đặc_biệt = {}
tổng_kí_hiệu_đặc_biệt = 0

for ky_tu in chuỗi:
    if not ky_tu.isalnum():
        kí_tự_đặc_biệt[ky_tu] = kí_tự_đặc_biệt.get(ky_tu, 0) + 1
        tổng_kí_hiệu_đặc_biệt += 1

for ky_tu, so_lan_xuat_hien in kí_tự_đặc_biệt.items():
    print(f"Số lần xuất hiện của ký tự '{ky_tu}': {so_lan_xuat_hien}")

if len(chuỗi) > 0:
    for ky_tu, so_lan_xuat_hien in kí_tự_đặc_biệt.items():
        ty_le = (so_lan_xuat_hien / len(chuỗi)) * 100
        print(f"Tỷ lệ phần trăm của ký tự '{ky_tu}': {ty_le:.2f}%")
else:
    print("Chuỗi không có ký tự nào!")

print("Tổng số ký tự đặc biệt trong chuỗi là: ", tổng_kí_hiệu_đặc_biệt)