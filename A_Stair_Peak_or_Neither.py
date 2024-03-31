n = int(input())

for _ in range(0, n):
    data = input().split(' ')
    if int(data[0]) < int(data[1]) < int(data[2]):
        print("STAIR")
    elif int(data[0]) < int(data[1]) > int(data[2]):
        print("PEAK")
    else:
        print("NONE")