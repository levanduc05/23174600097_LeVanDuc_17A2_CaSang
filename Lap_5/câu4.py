chuỗi_kí_tự = input("Nhập chuỗi ký tự: ")
chuỗi_số = ''.join(ky_tu for ky_tu in chuỗi_kí_tự if ky_tu.isdigit())

if chuỗi_số:
    số_nguyên = int(chuỗi_số)
    if số_nguyên > 1:
        for i in range(2, số_nguyên):
            if (số_nguyên % i) == 0:
                print(f"Chuỗi '{chuỗi_số}' không phải là số nguyên tố.")
                break
        else:
            print(f"Chuỗi '{chuỗi_số}' là số nguyên tố.")
    else:
        print(f"Chuỗi '{chuỗi_số}' không phải là số nguyên tố.")
else:
    print("Không có số nào trong chuỗi.")