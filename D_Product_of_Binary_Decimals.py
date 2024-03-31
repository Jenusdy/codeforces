test = int(input())

def is_binary_string(s):
    return all(char in {'0', '1'} for char in s)

for t in range(0,test):
    n = int(input())

    check = True
    if is_binary_string(str(n)):
        print("YES")
    else:
        hasil = ""
        s = 0
        while(n > 11):
            h = n // 11
            s = n % 11

            temp = str(h) + str(s)
            hasil += str(h)

            if h > s :
                n = h
            else :
                n = s

            if is_binary_string(temp):
                check = False
                print("YES")
                break
        
        
        if check : 
            temp_ = hasil + str(s)
            if is_binary_string(temp_):
                print("YES")
            else :
                print("NO")
    
