test = int(input())

for t in range(0,test):
    jam = input().split(":")

    if (int(jam[0]) < 12) and (int(jam[0]) > 0):
        print("{}:{} {}".format(jam[0], jam[1], "AM"))
    elif (int(jam[0]) == 12):
        print("{}:{} {}".format(jam[0], jam[1], "PM"))
    elif (int(jam[0]) > 12):
        print("{:02d}:{} {}".format(int(jam[0]) - 12, jam[1], "PM"))
    else:
        print("{:02d}:{} {}".format(int(jam[0]) + 12, jam[1], "AM"))