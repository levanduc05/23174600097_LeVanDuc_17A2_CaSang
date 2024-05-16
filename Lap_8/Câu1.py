def la_so_nguyen_to(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def in_cac_so_nguyen_to_sinh_doi(gioi_han_tren):
    for so in range(3, gioi_han_tren, 2):
        if la_so_nguyen_to(so) and la_so_nguyen_to(so + 2):
            print(f"({so}, {so + 2})")

in_cac_so_nguyen_to_sinh_doi(1000)
