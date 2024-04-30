n = int(input())

total = 0
temp = ''
for i in range(n):
    m = input()
    if m != temp:
        temp = m 
        total += 1
print(total)