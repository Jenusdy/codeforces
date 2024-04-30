year = input()

for i in range(int(year)+1,9999):
    y = set(list(str(i)))
    if len(y) >= 4:
        print(str(i))
        break