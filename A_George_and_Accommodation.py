n = int(input())

total = 0
for i in range(n):
    p, q = input().split(' ')
    p, q = list(map(int,[p,q]))
    if q - 2 >= p:
        total+=1
print(total)