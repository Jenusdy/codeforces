n = int(input())

total = 0
for i in range(0,n):
    op = input()
    if op == 'X++' or op == '++X':
        total += 1
    else : 
        total -= 1
print(total)