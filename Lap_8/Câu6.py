def la_so_le(n):
    return n % 2 != 0

def la_so_chan(n):
    return n % 2 == 0

def lap_phuong(n):
    return n ** 3

def binh_phuong(n):
    return n ** 2

danh_sach = list(map(int, input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ").split(',')))

danh_sach_binh_phuong_le = list(map(binh_phuong, filter(la_so_le, danh_sach)))

danh_sach_lap_phuong_chan = list(map(lap_phuong, filter(la_so_chan, danh_sach)))

print("Danh sách bình phương của các số lẻ:", danh_sach_binh_phuong_le)
print("Danh sách lập phương của các số chẵn:", danh_sach_lap_phuong_chan)
