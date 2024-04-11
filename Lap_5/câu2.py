str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

độ_dài_str1 = len(str1)
độ_dài_str2 = len(str2)

chuỗi_ngắn_nhất = ''
độ_dài_chuỗi_ngắn_nhất = min(độ_dài_str1, độ_dài_str2)

for i in range(độ_dài_chuỗi_ngắn_nhất ):
    if str1[i] == str2[i]:
        chuỗi_ngắn_nhất += str1[i]
    else:
        break

if chuỗi_ngắn_nhất:
    print("Chuỗi chung ngắn nhất:", chuỗi_ngắn_nhất)
else:
    print("Không có chuỗi chung nào.")