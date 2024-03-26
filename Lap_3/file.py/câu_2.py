# Các số chia hết cho 7 nhưng không chia hết cho 5
def tính_tổng():
    tổng = 0 
    for i in range (2000, 4001):
        if i % 7 == 0 and i % 5 != 0:
            tổng +=i
    return tổng
tong = tính_tổng()
print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 là :",tong)

#  Các số chia hết cho 4 nhưng không chia hết cho 6
def tính_tổng ():
    tong = 0
    for i in range (500,1001):
        if i % 4 == 0 and i % 6 !=0 :
            tong +=i
    return tong
print("Tổng các sô schia hết cho 4 nưng không chia hết 6 là :",tính_tổng())


