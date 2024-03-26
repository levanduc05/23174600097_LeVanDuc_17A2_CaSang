# In ra các số Fibonaci sao cho số cuồi cùng trong chuỗi nhỏ hơn 100
def so_fibo(n):
    flag=False 
    for i in day:
        if i==n:
            flag =True 
            return flag 

    return flag 

day=[0,1]                        
vonglap=[0]
for i in vonglap:
    vonglap.append(i+1)
    
    tong=day[i]+day[i+1]
    day.append(tong)
    if  tong >100 :
        break
for i in range (0 ,100):
    if so_fibo(i):
        print(i, end = " ")