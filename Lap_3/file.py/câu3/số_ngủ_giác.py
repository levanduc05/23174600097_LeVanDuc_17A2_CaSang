# IN ra tổng các số ngủ giác từ 1 đến 200
def ngu_giac(n):
    return n * (3 * n - 1) // 2
ngu_giac_list = []
for i in range(1, 201):
    số_ngủ_giác = ngu_giac(i)
    if số_ngủ_giác <= 200:
        ngu_giac_list.append(số_ngủ_giác)
    else:
        break
print("Các số ngũ giác từ 1 đến 200 là:")
print(ngu_giac_list)