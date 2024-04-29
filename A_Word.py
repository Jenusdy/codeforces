str1 = input()

counter = 0
for s in str1: 
    if s.isupper():
        counter+=1
    else:
        counter-=1

if counter > 0:
    print(str1.upper())
else:
    print(str1.lower())