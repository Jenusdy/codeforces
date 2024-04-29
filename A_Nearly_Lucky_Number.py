lucky_number = input()

lucky = [i for i in lucky_number if i in ['4','7']]
s = str(len(lucky))

res = True
for i in s:
    if s in ['4','7']:
        continue
    else :
        res = False
        break

if res:
    print("YES")
else: 
    print("NO")