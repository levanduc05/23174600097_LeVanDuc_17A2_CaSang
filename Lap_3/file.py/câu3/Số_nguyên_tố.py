# In ra các sôs nguyên tố từ 100 - 1000(tính cả số 1000)
def kiểm_tra_số_nguyên_tố(n):
    if n <= 1:
        return False 
    for i in range(2, n):
        if n % i == 0: 
            return False  
    return True

for i in range(100, 1001):
    if kiểm_tra_số_nguyên_tố(i):
        print(i, end =" ")