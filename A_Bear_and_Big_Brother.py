input = input().split(' ')
a,b = list(map(int, input))

tahun = 0
while b >= a:
    a = a*3
    b = b*2
    tahun+=1
print(tahun)