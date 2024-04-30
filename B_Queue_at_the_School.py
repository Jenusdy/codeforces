n, t = input().split(' ')
n, t = list(map(int, [n, t]))

q = list(input())


for i in range(t):
    flag = False
    for index in range(len(q) - 1):
        if q[index] == 'B' and q[index + 1] == 'G' and not flag:
            q[index], q[index + 1] = q[index + 1], q[index]
            flag = True
        else: 
            flag = False

print(''.join(q))