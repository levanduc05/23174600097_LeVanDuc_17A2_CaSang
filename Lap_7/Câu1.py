N = int(input("Nhập vào số nguyên N: "))
dictionary = {}

for i in range(1, N + 1):
    dictionary[i] = i ** 3

print("Từ điển dạng như sau:")
print(dictionary)
