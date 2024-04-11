chuỗi = input("Nhập một chuỗi có độ dài hơn 10 kí tự đi : ")

if len(chuỗi) > 10:
    # a
    chuoi_a = chuỗi[1:8]
    print("a, Chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8:", chuoi_a)
    # b
    chuoi_b = chuỗi[4:9]
    print("b, Chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5:", chuoi_b)
    # c
    chuoi_c = chuỗi[-3:]
    print("c, Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", chuoi_c)
    # d
    chuoi_d = chuỗi.lower()
    print("d, Chuỗi sau khi chuyển đổi thành chữ thường:", chuoi_d)
    # e
    chuoi_e = chuỗi.upper()
    print("e, Chuỗi sau khi chuyển đổi thành chữ hoa:", chuoi_e)
    # f
    chuoi_f = chuỗi[::-1]
    print("f, Chuỗi sau khi đảo ngược:", chuoi_f)
else:
    print("Chuỗi không có độ dài hơn 10 ký tự.")