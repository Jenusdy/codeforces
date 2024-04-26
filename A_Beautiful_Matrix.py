for i in range(0,5):
    baris = input().split()
    if '1' in baris:
        kolom = baris.index('1') + 1
        baris = i +1
        break

print(abs(3 - baris) + abs(3-kolom))