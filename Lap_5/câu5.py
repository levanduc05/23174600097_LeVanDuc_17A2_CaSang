chuỗi_1 = input("Nhập chuỗi thứ nhất: ")
chuỗi_2 = input("Nhập chuỗi thứ hai: ")
chuỗi = ''
do_dai_chuoi_ngan_nhat = min(len(chuỗi_1), len(chuỗi_2))

for i in range(do_dai_chuoi_ngan_nhat):
    chuỗi += chuỗi_1[i] + '-' + chuỗi_2[i] + '-'

chuỗi += chuỗi_1[do_dai_chuoi_ngan_nhat:] + '-' + chuỗi_2[do_dai_chuoi_ngan_nhat:]

chuỗi_trộn = chuỗi.rstrip('-')  

print("Chuỗi sau khi trộn:", chuỗi_trộn)