def cubesum(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10
    return total

def PrintArmstrong():
    print("Các số Armstrong từ 1 đến 999 là:")
    for num in range(1, 1000):
        if cubesum(num) == num:
            print(num)

def isArmstrong(n):
    return cubesum(n) == n

PrintArmstrong()

n = int(input("Nhập một số để kiểm tra xem nó có phải là số Armstrong không: "))
if isArmstrong(n):
    print(f"{n} là số Armstrong.")
else:
    print(f"{n} không phải là số Armstrong.")
