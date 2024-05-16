def sumPdivisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

m = int(input("Nhập một số để tính tổng các ước số chính của nó: "))
print(f"Tổng của các ước số chính của {m} là: {sumPdivisors(m)}")
