chuỗi_ban_đầu = input("Nhập chuỗi ban đầu của bạn nhanh lên đi:")
chuỗi_mới = input("Nhập chuỗi mới của bạn nhanh lên đi:")

if len(chuỗi_ban_đầu) != len(chuỗi_mới):
    print("Không thể thay đổi chuỗi!")
else:
    so_ky_tu_khac_nhau = 0
    for i in range(len(chuỗi_ban_đầu)):
        if chuỗi_ban_đầu[i] != chuỗi_mới[i]:
            so_ky_tu_khac_nhau += 1
    if so_ky_tu_khac_nhau <= 1:
        print("Có thể thay đổi chuỗi ban đầu thành 1 chuỗi mới!")
    else:
        print("Không thể thay đổi chuỗi ban đầu thành 1 chuỗi mới!")