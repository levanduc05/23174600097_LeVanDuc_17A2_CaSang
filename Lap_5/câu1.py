sothapphan = int(input("Nhập 1 số thập phân không âm nhé: "))

if sothapphan < 0:
    print("ơ kìa số nó âm rồi kìa ")
else:
    if sothapphan == 0:
        print("Số nhị phân tương ứng là : 0")
    else:
        nhiphan = ''
        while sothapphan > 0:
            nhiphan = str(sothapphan % 2) + nhiphan
            sothapphan //= 2
        print("Số nhị phân là:", nhiphan)