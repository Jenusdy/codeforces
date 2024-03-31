n = int(input())

for test in range(0,n):
    t = int(input())
    for i in range(1,2*t + 1):
        for j in range(1,2*t + 1):
            if j != 2*t:
                print('#',end="")
            else:
                print('#')