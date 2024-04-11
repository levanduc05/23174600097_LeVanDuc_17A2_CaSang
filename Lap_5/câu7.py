chuỗi = input("Nhập chuỗi của bạn đi nào: ")

số_chữ_thường = 0
số_chữ_hoa = 0
số_chữ_số = 0
số_kí_hiệu_đặc_biệt = 0

for ky_tu in chuỗi:
    if ky_tu.islower():
        số_chữ_thường += 1
    elif ky_tu.isupper():
        số_chữ_hoa += 1
    elif ky_tu.isdigit():
        số_chữ_số += 1
    else:
        số_kí_hiệu_đặc_biệt += 1

print("Số lượng chữ thường trong chuỗi:", số_chữ_thường)
print("Số lượng chữ hoa trong chuỗi:", số_chữ_hoa)
print("Số lượng chữ số trong chuỗi:", số_chữ_số)
print("Số lượng ký tự đặc biệt trong chuỗi:", số_kí_hiệu_đặc_biệt)