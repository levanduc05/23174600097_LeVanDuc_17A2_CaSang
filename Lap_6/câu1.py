n = int(input("Nhập số lượng phần tử trong mảng: "))
mang = []
print("Nhập các phần tử của mảng:")
for i in range(n):
    num = int(input(f"Phần tử {i+1}: "))
    mang.append(num)

tong_chan = 0
tong_le = 0
for num in mang:
    if num % 2 == 0:
        tong_chan += num
    else:
        tong_le += num

print("Tổng của tất cả các số chẵn trong mảng là:", tong_chan)
print("Tổng của tất cả các số lẻ trong mảng là:", tong_le)
