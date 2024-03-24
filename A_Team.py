n = int(input())

def toInt(n):
    return int(n)

total = 0
for _ in range(1,n+1):
    choices = input().split(' ')
    choices = list(map(toInt, choices))
    if sum(choices) > 1 :
        total+=1
print(total)
