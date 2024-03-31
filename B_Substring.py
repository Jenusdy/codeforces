str = input()
str_len = len(str)

temp = []
for i in range(str_len):
    for j in range(i+1):
        subs = str[j:i+1]
        if subs not in temp:
            temp.append(subs)

print(len(temp))