n = int(input())

max = 0
passanger = 0
for i in range(n):
    a,b = input().split(' ')
    a,b = list(map(int,[a,b]))
    passanger = passanger + (b - a)
    if passanger > max :
        max = passanger

print(max)