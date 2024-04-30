n,h = input().split(' ')
a = input().split(' ')
a = list(map(int, a))
n,h = list(map(int, [n,h]))

height = 0
for i in a:
    if i <= h:
        height += 1
    else:
        height += 2
print(height)