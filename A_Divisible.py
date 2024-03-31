n, k = input().split(' ')

list_ = input().split(' ')
list_ = list(map(int, list_))

hasil = []
for i in list_:
    if i % int(k) == 0:
        hasil.append(int(i/int(k)))

print(*hasil)