# Câu a 
tổng = 0 
số= 0 
while tổng <= 1000:
    h = int(input("Nhập vào một số h"))
    số = số + 1
    if h % 2 != 0 :
        tổng+=h
    print(tổng)

#Câu b
tổng = 0
số_z = 0
while tổng <= 1000 :
    h = int(input("Nhập vào một số h"))
    số = số + 1
    if h%2 == 0 :
        tổng+=h
    print(tổng)

# Câu c
print(f"Số lượng số nguyên đã nhập vào là : {số+số_z}")
