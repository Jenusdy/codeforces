n, k = input().split(' ')
n, k = list(map(int, [n,k]))

for i in range(k):
    if n % 10 == 0:
        n = int(n/10)
    else:
        n = n -1
print(n)