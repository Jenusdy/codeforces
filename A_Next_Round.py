temp = input().split(' ')
n = int(temp[0])
k = int(temp[1])

temp = input().split(' ')
score = [ int(x) for x in temp ]

batas = score[k-1]

def isAdvance(n, batas):
    if n >= batas and n > 0:
        return 1
    return 0

result = [isAdvance(x, batas) for x in score]

print(sum(result))