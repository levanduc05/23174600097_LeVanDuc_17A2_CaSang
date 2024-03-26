#In ra các số chính phương từ 1 đến 1000
def kiểm_tra(n):
    if n <0 :
        flag= False
        return False
    for i in range(1,n):
        if i*i == n :
            flag = False
            return True
    return False

for i in range(1,101):
    if kiểm_tra(i):
        print(i, end=" ")