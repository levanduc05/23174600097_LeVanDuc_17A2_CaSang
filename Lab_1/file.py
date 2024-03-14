# Bài 1------------------------------------------------------------------
print("""
i carry your heart with me (i carry it in
my heart) i am never without it (anywhere
i go you go, my dear; and whatever is done
by only me is your doing, my darling)
i fear no fate (for you are my fate, my sweet)
i want no world (for beautiful you are my world, my true)
and it's you are whatever a moon has always meant
and whatever a sun will always sing is you
here is the deepest secret nobody knows
(here is the root of the root and the bud of the bud
and the sky of the sky of a tree called life; which grows
higher than soul can hope or mind can hide)
and this is the wonder that's keeping the stars apart
i carry your heart (i carry it in my heart)
---i carry your heart with me by e.e. cummings--
""")
# Bài 2----------------------------------------------------------------
# Hàm nhập thông tin sách từ bàn phím
def nhap_thong_tin_sach():
    ma_sach = input("Nhập mã sách (mã sinh viên): ")
    ten_sach = input("Nhập tên sách: ")
    tac_gia = input("Nhập tên tác giả: ")
    nam_xuat_ban = input("Nhập năm xuất bản: ")
    so_luong_sach = input("Nhập số lượng sách (ngày sinh của sinh viên): ")
    return ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong_sach

# Hàm in thông tin sách
def in_thong_tin_sach(ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong_sach):
    print(f"Thư viện ĐHKTKTCN có {so_luong_sach} sách '{ten_sach}' với mã số {ma_sach}.")
    print(f"Cuốn sách của tác giả {tac_gia} được xuất bản vào năm {nam_xuat_ban}")

# Chương trình chính
def main():
    ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong_sach = nhap_thong_tin_sach()
    in_thong_tin_sach(ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong_sach)

# Chạy chương trình
if __name__ == "__main__":
    main()

# Bài 3--------------------------------------------------------------
tiền_ban_đầu = 1000
lãi_suất = 0.06 
# Tiền lãi sau 5 năm
amount_after_5_years = tiền_ban_đầu*(1+lãi_suất)**5
#Tiền lãi sau 10 năm
amount_after_10_years = tiền_ban_đầu*(1+lãi_suất)**10
# Tỷ lệ tăng trưởng
growth_rate = (amount_after_10_years-amount_after_5_years)/amount_after_5_years
# IN ra màn hình
print(f"Số tiền sau 5 năm: ${amount_after_5_years:.2f}")
print(f"Số tiền sau 10 năm: ${amount_after_10_years:.2f}")
print(f"Tỷ lệ tăng trưởng giữa số tiền sau 10 năm so với sau 5 năm: {growth_rate * 100:.2f}%")

# BÀi 4--------------------------------------------------------------------
import math
a = float(input("Độ dài cạnh đấy: "))
h = float(input("chiều cao của hình chóp: "))

# Tính chiều cao của một mặt tam giác bên 
chiều_cao = math.sqrt(h**2 + (a / 2)**2)
# Tính diện tích xung quanh
diện_tích_xq = 2 * a * chiều_cao
# Tính diện tích đáy
diện_tích_đáy = a**2
# Tính diện tích toàn phần
diện_tích_tp = diện_tích_xq + diện_tích_đáy
# Tính thể tích
V = (1/3) * diện_tích_đáy* h
# In kết quả với 2 chữ số thập phân
print(f"Diện tích xung quanh: {diện_tích_xq:.2f}")
print(f"Diện tích toàn phần: {diện_tích_tp:.2f}")
print(f"Thể tích: {V:.2f}")

#Bài 5----------------------------------------------------------------------------
U = 220  
I = 1.5  
GIA_DIEN = 5000  

def tinh_tien_dien(so_gio_su_dung):
    
    P = U * I 

    
    dien_nang_tieu_thu = P * so_gio_su_dung / 1000  


    tien_dien = dien_nang_tieu_thu * GIA_DIEN

    return tien_dien

so_gio_su_dung = float(input("Nhập số giờ sử dụng máy lọc không khí: "))

tien_dien = tinh_tien_dien(so_gio_su_dung)
print(f"Tổng số tiền điện phải trả cho việc sử dụng máy lọc không khí là: {tien_dien:.2f} đồng")

# Bài 6 --------------------------------------------------------------------------
import math

def nhap_vecto(ten_vecto):
    x = float(input(f"Nhập hoành độ {ten_vecto}: "))
    y = float(input(f"Nhập tung độ {ten_vecto}: "))
    return (x, y)

def cong_vecto(a, b):
    return (a[0] + b[0], a[1] + b[1])

def tru_vecto(a, b):
    return (a[0] - b[0], a[1] - b[1])

def do_dai_vecto(v):
    return math.sqrt(v[0]**2 + v[1]**2)

def tich_vo_huong(a, b):
    return a[0]*b[0] + a[1]*b[1]

def cosin_goc(a, b):
    return tich_vo_huong(a, b) / (do_dai_vecto(a) * do_dai_vecto(b))

# Nhập tọa độ vectơ
a = nhap_vecto("a")
b = nhap_vecto("b")

# Phép cộng và phép trừ vectơ
vecto_cong = cong_vecto(a, b)
vecto_tru = tru_vecto(a, b)
print(f"Vectơ a + b = {vecto_cong}")
print(f"Vectơ a - b = {vecto_tru}")

# Độ dài vectơ
do_dai_a = do_dai_vecto(a)
do_dai_b = do_dai_vecto(b)
print(f"Độ dài vectơ a: {do_dai_a:.2f}")
print(f"Độ dài vectơ b: {do_dai_b:.2f}")

# Cosin của góc hợp giữa 2 vectơ
cosin = cosin_goc(a, b)
print(f"Cosin của góc giữa vectơ a và b: {cosin:.2f}")

# Bài 7--------------------------------------------------------------------------
def nhap_he_so():
    a1 = float(input("Nhập a1: "))
    b1 = float(input("Nhập b1: "))
    c1 = float(input("Nhập c1: "))
    a2 = float(input("Nhập a2: "))
    b2 = float(input("Nhập b2: "))
    c2 = float(input("Nhập c2: "))
    return a1, b1, c1, a2, b2, c2

def giai_he_phuong_trinh(a1, b1, c1, a2, b2, c2):
    D = a1*b2 - a2*b1
    Dx = c1*b2 - c2*b1
    Dy = a1*c2 - a2*c1
    if D == 0:
        if Dx == 0 and Dy == 0:
            return "Hệ phương trình có vô số nghiệm."
        else:
            return "Hệ phương trình vô nghiệm."
    else:
        x = Dx / D
        y = Dy / D
        return f"Hệ phương trình có nghiệm x = {x:.2f}, y = {y:.2f}"

a1, b1, c1, a2, b2, c2 = nhap_he_so()
ket_qua = giai_he_phuong_trinh(a1, b1, c1, a2, b2, c2)
print(ket_qua)

# BÀi 8-----------------------------------------------------------------------
import math
def tính_biểu_thức(x, z):
    f= x**2*math.sin(z) + math.sqrt(abs(x))
    p= math.log(z) + math.exp(x-1)
    t= math.atan(x*z)
    biểu_thức_F = f/p + t
    return biểu_thức_F
x=float(input("Nhập vào một số x : "))
z=float(input("Nhập vào một số z :"))
kết_quả= tính_biểu_thức(x, z)
print(f"Giá trị của biểu thức là: {kết_quả:.2f}")

#Bài 9-----------------------------------------------------------------------
def nhap_toa_do_diem(ten_diem):
    x = float(input(f"Nhập hoành độ {ten_diem}: "))
    y = float(input(f"Nhập tung độ {ten_diem}: "))
    return (x, y)

def tinh_trung_diem(diem1, diem2):
    return ((diem1[0] + diem2[0]) / 2, (diem1[1] + diem2[1]) / 2)

# Nhập tọa độ các đỉnh của tứ giác
M = nhap_toa_do_diem("M")
N = nhap_toa_do_diem("N")
P = nhap_toa_do_diem("P")
Q = nhap_toa_do_diem("Q")

# Tính tọa độ trung điểm của mỗi cạnh
trung_diem_MN = tinh_trung_diem(M, N)
trung_diem_NP = tinh_trung_diem(N, P)
trung_diem_PQ = tinh_trung_diem(P, Q)
trung_diem_QM = tinh_trung_diem(Q, M)

# In ra tọa độ trung điểm của mỗi cạnh
print(f"Trung điểm của cạnh MN: {trung_diem_MN}")
print(f"Trung điểm của cạnh NP: {trung_diem_NP}")
print(f"Trung điểm của cạnh PQ: {trung_diem_PQ}")
print(f"Trung điểm của cạnh QM: {trung_diem_QM}")

#Bài 10 ---------------------------------------------------------------------
from math import comb

def tinh_xac_suat(k):
    total_ways = comb(50, k)
    # Tất cả là bi đỏ
    red_ways = comb(20, k)
    p_red = red_ways / total_ways
    
    # Ít nhất một viên là bi xanh
    no_blue_ways = comb(35, k)
    p_at_least_one_blue = 1 - (no_blue_ways / total_ways)
    
    # Đúng hai viên là bi vàng
    if k >= 2:
        yellow_ways = comb(15, 2) * comb(35, k-2)
        p_exactly_two_yellow = yellow_ways / total_ways
    else:
        p_exactly_two_yellow = 0
    
    return p_red, p_at_least_one_blue, p_exactly_two_yellow

k = int(input("Nhập số lượng viên bi muốn rút: "))

p_red, p_at_least_one_blue, p_exactly_two_yellow = tinh_xac_suat(k)
print(f"Xác suất tất cả là bi đỏ: {p_red:.4f}")
print(f"Xác suất ít nhất một viên là bi xanh: {p_at_least_one_blue:.4f}")
print(f"Xác suất đúng hai viên là bi vàng: {p_exactly_two_yellow:.4f}")

