chuỗi_văn_bản = input("nhập chuỗi văn bản của bạn đi: ")
từ_cần_tìm = input("bạn tìm kiếm cái gì: ")

vị_trí_của_từ = chuỗi_văn_bản.find(từ_cần_tìm)

if vị_trí_của_từ != -1:
    print("Từ", từ_cần_tìm, "được tìm thấy tại vị trí:", vị_trí_của_từ)
else:
    print("Từ", từ_cần_tìm, "không được tìm thấy trong chuỗi.")

danh_sách_của_từ = chuỗi_văn_bản.split()
tần_số_xuất_hiện = {}
for tu in danh_sách_của_từ:
    tần_số_xuất_hiện[tu] = tần_số_xuất_hiện.get(tu, 0) + 1

tu_xuat_hien_nhieu_nhat = max(tần_số_xuất_hiện, key=tần_số_xuất_hiện.get)
tan_so_xuat_hien_nhieu_nhat = tần_số_xuất_hiện[tu_xuat_hien_nhieu_nhat]

print("Từ xuất hiện nhiều nhất trong chuỗi là:", tu_xuat_hien_nhieu_nhat)
print("Tần số xuất hiện:", tan_so_xuat_hien_nhieu_nhat)