n = int(input())
i = input().split(' ')
i = list(map(int, i))

try:
    i.index(1)
    print("HARD")
except ValueError:
    print("EASY") 