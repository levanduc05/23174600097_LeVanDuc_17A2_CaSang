# In ra các số haonf hảo bé hơn 500
def so_hoan_hao(n):
    flag=False
    tong=0 
    for i in range (1,n):
        tong=tong+i
        if tong==n:
            flag=True 
            return flag 
    return flag 
for i in range(1,500):
    if so_hoan_hao(i):
        print(i , end = " ")