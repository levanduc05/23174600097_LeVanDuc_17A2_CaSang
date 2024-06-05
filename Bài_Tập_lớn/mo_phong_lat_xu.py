import random
import csv

ket_qua_lat_xu = []

cac_ket_qua_da_xuat_hien = set()

xac_suat = {"Ngửa": 0.7, "Sấp": 0.3}
so_lan_xuat_hien = {"Ngửa": 0, "Sấp": 0}

def lat_xu():
    ket_qua = random.choices(["Ngửa", "Sấp"], weights=[0.7, 0.3])[0]
    return ket_qua


def tinh_xac_suat(ket_qua_lat_xu):
    tong_so_lan_lat = len(ket_qua_lat_xu)
    so_lan_xuat_hien = {"Ngửa": ket_qua_lat_xu.count("Ngửa"), "Sấp": ket_qua_lat_xu.count("Sấp")}
    xac_suat_thuc_te = {key: value / tong_so_lan_lat for key, value in so_lan_xuat_hien.items()}
    return so_lan_xuat_hien, xac_suat_thuc_te


def hien_thi_lich_su_lat_xu(ket_qua_lat_xu):
    for idx, ket_qua in enumerate(ket_qua_lat_xu, 1):
        print(f"Lần lật {idx}: {ket_qua}")

so_lan_lat = 1000

for _ in range(so_lan_lat):
    ket_qua = lat_xu()
    ket_qua_lat_xu.append(ket_qua)
    cac_ket_qua_da_xuat_hien.add(ket_qua)

print("Lật xu hoàn tất.")

so_lan_xuat_hien, xac_suat_thuc_te = tinh_xac_suat(ket_qua_lat_xu)

print("Tính xác suất hoàn tất.")
print("Số lần xuất hiện và xác suất thực tế:")
for ket_qua in so_lan_xuat_hien:
    print(f"{ket_qua}: {so_lan_xuat_hien[ket_qua]} lần, xác suất {xac_suat_thuc_te[ket_qua]:.4f}")

with open('ket_qua_lat_xu.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Kết Quả", "Số Lần Xuất Hiện", "Xác Suất"])
    for ket_qua in so_lan_xuat_hien:
        writer.writerow([ket_qua, so_lan_xuat_hien[ket_qua], xac_suat_thuc_te[ket_qua]])

print("Lưu file CSV hoàn tất.")

hien_thi_lich_su_lat_xu(ket_qua_lat_xu)
