def giai_thua(n):
    if n == 0 & n == 1:
        return 1
    ket_qua = 1
    for i in range(2, n + 1):
        ket_qua *= i
    return ket_qua

def hoan_vi(n, r):
    return giai_thua(n) // giai_thua(n - r)

def to_hop(n, r):
    return hoan_vi(n, r) // giai_thua(r)

n = int(input("Nhập n: "))
r = int(input("Nhập r: "))

print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần là: P({n}, {r}) = {hoan_vi(n, r)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần là: C({n}, {r}) = {to_hop(n, r)}")
