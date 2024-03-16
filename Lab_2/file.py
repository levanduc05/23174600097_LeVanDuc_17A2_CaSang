# Bài 1--------------------------------------------
def phương_trình_bậc_nhất(a, b):
    if a==0 :
        if b == 0 :
            print("Nghiệm đúng với mọi x ")
        else :
            print("Phương trình vô nghiệm")
    if a !=0 :
        x = -b/a
        print("Phương trình có nghiệm là : ", x )
a = float(input("Nhập vào một số a :"))
b = float(input("Nhập vào một số b :"))
print(phương_trình_bậc_nhất(a, b))
 #Bài 2 --------------------------------------------
def số_hàng_nghìn(số_nguyên):
    if len(str(số_nguyên)) >= 4:
        số = int(str(số_nguyên)[-4])
        print("Chữ số hàng nghìn là:", số)
    else:
        print("Không có chữ số hàng nghìn, xuất ra 0.")
so_nguyen = int(input("Nhập một số nguyên: "))
print(số_hàng_nghìn(so_nguyen))

# Bài 3 ----------------------------------------
def doc_so_nguyen_tieng_anh(so_nguyen):
    # Tạo các từ điển số từ 0 đến 19 và từ 20 đến 90
    num_dict_0_to_19 = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }
    num_dict_20_to_90 = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
    }

    # Chia số nguyên thành các chữ số
    hang_tram = so_nguyen // 100
    so_con_lai = so_nguyen % 100

    # Tạo chuỗi kết quả
    ket_qua = ''

    # Xử lý hàng trăm
    if hang_tram > 0:
        ket_qua += num_dict_0_to_19[hang_tram] + ' hundred'

    # Xử lý số còn lại
    if so_con_lai > 0:
        if hang_tram > 0:
            ket_qua += ' and '

        if so_con_lai < 20:
            ket_qua += num_dict_0_to_19[so_con_lai]
        else:
            hang_chuc = so_con_lai // 10
            hang_don_vi = so_con_lai % 10
            ket_qua += num_dict_20_to_90[hang_chuc]
            if hang_don_vi > 0:
                ket_qua += '-' + num_dict_0_to_19[hang_don_vi]

    return ket_qua

# Nhập số nguyên có ba chữ số từ người dùng
so_nguyen = int(input("Nhập một số nguyên có ba chữ số: "))

# Kiểm tra xem số nguyên có ba chữ số không
if 100 <= so_nguyen <= 999:
    # Gọi hàm để đọc số nguyên theo tiếng Anh và in ra
    print("Cách đọc của số nguyên này là:", doc_so_nguyen_tieng_anh(so_nguyen))
else:
    print("Số nguyên nhập không hợp lệ, vui lòng nhập lại.")

# Bài 4 ---------------------------------------
def kiểm_tra_điểm(x):
    flag = True
    if x < 0 :
        return flag
    if x <= 5 and x >=0 :
        print("Điểm kém ")
    elif x>5 and x<=7 :
        print("Điểm trung bình")
    elif x <7 and x<=8.5 :
        print("Điểm khá ")
    elif x>8.5 and x <= 10 :
        print("Điểm giỏi")
    return 
x= float(input("Nhập vào một số : "))
print(kiểm_tra_điểm(x))

# Bài 5 ---------------------------
def giá_vé(số_người):
    giá_vé_1_người = 120000
    tổng_tiền = giá_vé_1_người*số_người
    flag = True
    if số_người < 0 :
        return flag
    elif số_người==1:
        tiền = giá_vé_1_người
        print("Số tiền phải trả là : ", tiền)
    elif số_người >= 2 and số_người <=4 :
        tiền = tổng_tiền * (100-5/100)
        print("Số tiền phải trả là :", tiền)
    elif số_người >4 and số_người <=10 :
        tiền = tổng_tiền * (100-10/100)
        print("Số tiền phải trả là :" , tiền)
    elif số_người >10 :
        tiền = tổng_tiền * (100-20/100)
        print("Số tiền phải trả là :", tiền)
        return 
    return 
số_người = int(input("Nhập số người muốn mua vé :"))
print(giá_vé(số_người))

# Bài 6 -----------------------------------
def tìm_số(a, b, c):
    if a >= b and a >= c:
        if b >= c:
            return b
        else:
            return c
    elif b >= a and b >= c:
        if a >= c:
            return a
        else:
            return c
    else:
        if a >= b:
            return a
        else:
            return b
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
Số_lớn = tìm_số(a, b, c)
print("Số lớn thứ hai trong ba số nguyên là:", Số_lớn)

# Bài 7 ----------------------------------------------
def BMI(cân_nặng):
    flag = True
    if cân_nặng < 0 :
        return flag
    elif cân_nặng <= 18.5 :
        print("Bạn gầy quá rồi đó")
    elif cân_nặng >18.5 and cân_nặng <=24.9 :
        print("Bạn đang bình thường đó nha")
    elif cân_nặng >= 25.0 and cân_nặng <=29.9 :
        print("Bạn có hơi béo đó")
    elif cân_nặng >= 30.0 :
        print("Ôi bạn ôi ! BẠn quá béo rồi đó nha ")
        return
    return
cân_nặng = float(input("Hãy nhập cân nặng của bạn vào đây : "))
print(BMI(cân_nặng))

# Bài 8-----------------------------------------------
def vị_trí_tương_đối(m1, b1, m2, b2):
    if m1 == m2:
        if b1 == b2:
            return "Hai đường thẳng trùng nhau"
        else:
            return "Hai đường thẳng song song"
    elif m1 * m2 == -1:
        return "Hai đường thẳng vuông góc"
    else:
        return "Hai đường thẳng cắt nhau"
m1 = float(input("Nhập hệ số góc của đường thẳng thứ nhất: "))
b1 = float(input("Nhập hệ số tự do của đường thẳng thứ nhất: "))
m2 = float(input("Nhập hệ số góc của đường thẳng thứ hai: "))
b2 = float(input("Nhập hệ số tự do của đường thẳng thứ hai: "))
vi_tri = vị_trí_tương_đối(m1, b1, m2, b2)
print("Vị trí tương đối của hai đường thẳng là:", vi_tri)

# Bài 9 ------------------------------------------------
import math

def khoang_cach_diem_den_duong_thang(m, b, x0, y0):
    # Tính khoảng cách từ một điểm đến đường thẳng
    return abs(m * x0 - y0 + b) / math.sqrt(m**2 + 1)

def kiem_tra_vi_tri_duong_thang_va_duong_tron(m, b, x0, y0, ban_kinh):
    khoang_cach = khoang_cach_diem_den_duong_thang(m, b, x0, y0)
    if khoang_cach < ban_kinh:
        return "Đường thẳng cắt đường tròn"
    elif khoang_cach == ban_kinh:
        return "Đường thẳng tiếp xúc đường tròn"
    else:
        if khoang_cach < ban_kinh + 0.000001:
            return "Đường thẳng nằm trong đường tròn"
        else:
            return "Đường thẳng nằm ngoài đường tròn"

# Nhập thông số của đường thẳng
m = float(input("Nhập hệ số góc của đường thẳng: "))
b = float(input("Nhập hệ số tự do của đường thẳng: "))

# Nhập thông số của đường tròn
x0 = float(input("Nhập hoành độ tâm của đường tròn: "))
y0 = float(input("Nhập tung độ tâm của đường tròn: "))
ban_kinh = float(input("Nhập bán kính của đường tròn: "))

# Kiểm tra vị trí tương đối giữa đường thẳng và đường tròn
vi_tri = kiem_tra_vi_tri_duong_thang_va_duong_tron(m, b, x0, y0, ban_kinh)

# In ra kết quả
print("Vị trí tương đối giữa đường thẳng và đường tròn là:", vi_tri)

# BÀi 10-------------------------------------------------
def hien_thi_phim_va_khung_gio(thể_loại_phim):
    for thể_loại, phim_khung_gio in thể_loại_phim.items():
        print(f"\n{thể_loại}:")
        for i, (phim, khung_gio) in enumerate(phim_khung_gio.items(), 1):
            print(f"{i}. {phim}: {', '.join(khung_gio)}")

def main():
    thể_loại_phim = {
        "Hành động": {
            "1. The Marksman - Tay Xạ Thủ (2021)": ["sáng", "trưa", "chiều", "tối"],
            "2. Godzilla and Kong - Godzilla đại chiến Kong": ["sáng", "trưa", "chiều", "tối"],
            "3. Fast & Furious 9 - Quá nhanh quá nguy hiểm 9": ["sáng", "trưa", "chiều", "tối"],
            "4. Black Widow - Góa phụ đen": ["sáng", "trưa", "chiều", "tối"],
            "5. Spider - Man: No Way Home - Người Nhện: Không Còn Nhà": ["sáng", "trưa", "chiều", "tối"]
        },
        "Kinh dị": {
            "6. Ma Cây Trỗi Dậy - Evil Dead Rise (2023)": ["tối"],
            "7. Tà Chú Cấm - Home for Rent (2023)": ["tối"],
            "8. Năm Đêm Kinh Hoàng - Five Nights at Freddy's (2023)": ["tối"],
            "9. Phong Ấn Quỷ Dữ - It Lives Inside (2023)": ["tối"],
            "10. Quỷ Ám: Tín Đồ - The Exorcist: Believer (2023)": ["tối"]
        },
        "Tình cảm": {
            "11. Nhà Bà Nữ (2023) - Phim tình cảm chiếu rạp Việt Nam": ["tối"],
            "12. Titanic (1997) - Phim tình cảm Mỹ kinh điển": ["tối"],
            "13. Vũ Điệu Samba (2004) - Phim tình cảm Hàn Quốc": ["tối"],
            "14. Đã Đến Lúc (2013) - Phim tình cảm Mỹ hài hước": ["tối"],
            "15. Pride & Prejudice (2005) - Phim tình cảm Anh cổ điển": ["tối"]
        },
        "Hài hước": {
            "16. Deadpool (2016) Những kẻ bên lề": ["sáng", "trưa", "chiều", "tối"],
            "17. The intouchables (2011) Trở về tương lai": ["sáng", "trưa", "chiều", "tối"],
            "18. Back to the Future (1985) Cuộc đời tuyệt vời của Amélie Poulain": ["sáng", "trưa", "chiều", "tối"],
            "19. Le fabuleux destin Amélie Poulain (2001) Vút bay": ["sáng", "trưa", "chiều", "tối"],
            "20. Up (2009)": ["sáng", "trưa", "chiều", "tối"]
        },
        "Hoạt hình": {
            "21. Vua Sư Tử (The Lion King)": ["sáng", "trưa", "chiều", "tối"],
            "22. Đi tìm Nemo (Finding Nemo)": ["sáng", "trưa"],
            "23. Câu chuyện đồ chơi 3 (Toy Story 3)": ["sáng", "trưa"],
            "24. Up (vút bay)": ["sáng", "trưa"],
            "25. Nữ Hoàng Băng Giá (Frozen)": ["sáng", "trưa"]
        }
    }

    print("Chào mừng bạn đến với rạp phim!")
    print("Dưới đây là các thể loại phim bạn có thể lựa chọn:")
    for i, thể_loại in enumerate(thể_loại_phim.keys(), 1):
        print(f"{i}. {thể_loại}")

    while True:
        try:
            lựa_chọn_thể_loại = int(input("Nhập số thứ tự của thể loại phim bạn muốn xem: "))
            if 1 <= lựa_chọn_thể_loại <= len(thể_loại_phim):
                break
            else:
                print("Vui lòng nhập một số trong phạm vi từ 1 đến", len(thể_loại_phim))
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

    index_thể_loại = 0
    for i, (thể_loại, phim_khung_gio) in enumerate(thể_loại_phim.items(), 1):
        if i == lựa_chọn_thể_loại:
            index_thể_loại = i
            break

    print(f"Bạn đã chọn thể loại phim: {list(thể_loại_phim.keys())[index_thể_loại-1]}")
    print("Dưới đây là các phim và khung giờ chiếu:")
    có_suất_chiếu = False
    danh_sách_lựa_chọn_phim = []
    for phim, khung_gio in thể_loại_phim[list(thể_loại_phim.keys())[index_thể_loại-1]].items():
        if ("Tình cảm" in thể_loại_phim.keys() and phim in thể_loại_phim["Tình cảm"]) and "tối" not in khung_gio:
            continue
        if ("Hoạt hình" in thể_loại_phim.keys() and phim in thể_loại_phim["Hoạt hình"]) and "sáng" not in khung_gio and "trưa" not in khung_gio:
            continue
        if ("Kinh dị" in thể_loại_phim.keys() and phim in thể_loại_phim["Kinh dị"]) and "tối" not in khung_gio:
            continue

        có_suất_chiếu = True
        print(f"{phim}: {', '.join(khung_gio)}")
        danh_sách_lựa_chọn_phim.append(phim)

    if not có_suất_chiếu:
        print("Không có suất chiếu.")
    else:
        while True:
            lựa_chọn_phim = input("Nhập số của phim bạn muốn xem: ")
            if lựa_chọn_phim.isdigit() and 1 <= int(lựa_chọn_phim) <= len(danh_sách_lựa_chọn_phim):
                index_phim = int(lựa_chọn_phim) - 1
                phim_đã_chọn = danh_sách_lựa_chọn_phim[index_phim]
                print(f"Bạn đã chọn phim '{phim_đã_chọn}'")

                while True:
                    lựa_chọn_khung_giờ = input("Nhập khung giờ bạn muốn xem (sáng/trưa/chiều/tối): ").strip().lower()
                    if lựa_chọn_khung_giờ in thể_loại_phim[list(thể_loại_phim.keys())[index_thể_loại-1]][phim_đã_chọn]:
                        print(f"Phim '{phim_đã_chọn}' sẽ được chiếu vào khung giờ {lựa_chọn_khung_giờ}.")
                        break
                    else:
                        print("Khung giờ không hợp lệ.")
                break
            else:
                print("Vui lòng nhập một số từ 1 đến", len(danh_sách_lựa_chọn_phim))

if __name__ == "__main__":
    main()





    




